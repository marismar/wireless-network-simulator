from package import package
from table import route_table
import logging

class Network_layer:

    _id_pck = 0

    def __init__(self,host):
        self.host = host
        self.pending_pck = []
        self.received_pck = []
        self.table = route_table(host)
        # temporary route table 

    def add_received_pck(self, pck_id):
        try:
            self.received_pck.index(pck_id)
        except :
            self.received_pck.append(pck_id)
            return True
        return False


    #Function to CREATE and SEND a DATA pck to **LINK LAYER**
    def send_pck(self,message,destination):
        if len(message) > 0 :	#check if message is valid
            # print for debugging
            print('* '*20)
            print("* Creating a package in network_layer *")
            print('* '*20, '\n')

            #new package with the message
            pck = package(Network_layer._id_pck,'DATA',message,self.host.get_mac(),destination)
            logging.info(f' Created a DATA package from host[{self.host.get_mac()}] to host[{destination}]')
            
            pck.package_info() # prints the package information
            Network_layer._id_pck += 1 # update the id

            # checks if the destination is my neighbor
            nb = self.host.get_neighbors()
            var = False
            for obj in nb:
                if destination == obj.get_mac():
                    var = True
                    break    

            # destination is a host's neighbor
            if var:
                logging.info(f' Host{destination} is my neighbor, so I can send')
                self.host.link.sending_request(pck)

            # if is not my neighbor, then check if I have a way to him
            if self.table.get_route() != {}:
                print("\033[36m\t\tL3: I HAVE A ROUTE TABLE, BUT I DO NOT KNOW IF I HAVE DESTINY ON IT \033[37m")
                # set the next jump
                next_jp = self.table.next_jump(destination, self.host)
                
                if next_jp:
                    logging.info(f' I(host{self.host.get_mac()}) can get into the destination')
                    logging.info(f' And the next jump is to host[{next_jp}]')
                    pck.add_path(self.host)
                    pck.add_next(next_jp)
                    self.host.link.sending_request(pck)
            
            # if the host can't get into the destination, then it make a RREQ
            else :
                print(f"\033[36m +++++++++ L3: HOST{self.host.get_mac()} HAS NO ROUTE TO {destination}\033[37m")
                logging.info(f' I am host[{self.host.get_mac()}] and do not have a route for {destination} yet')
                self.create_RREQ_pck(pck)
            

    # create a REQUEST pck and send to link_layer
    def create_RREQ_pck(self,pck):
        self.pending_pck.append(pck) # save the package to send later
        
        pck_RREQ = package(Network_layer._id_pck,'RREQ',"I am a RREQ",self.host.get_mac(),pck.get_destination())
        Network_layer._id_pck += 1
        # if the host makes this type of pck, is saves to a list, so it won't send again
        self.received_pck.append(pck_RREQ.get_id())
        
        # print for debugging
        print(f'\t\t\033[36m HOST[{self.host.get_mac()}] IS CREATING A RREQ TO {pck.get_destination()}\033[37m\n')
        print(f'\t\t\033[36m HOST[{self.host.get_mac()}] IS ADDING ITSELF TO THE PATH\033[37m\n')
        
        # log print
        logging.info(f' Host[{self.host.get_mac()}] created a RREQ pack to host[{pck.get_destination()}]')
        logging.info(f' I am adding myself to the path')

        pck_RREQ.add_path(self.host) # adding itself on the path
        self.host.link.sending_request(pck_RREQ) # send a request to master
        

    # create a REPLY pck and send to link_layer
    def create_RREP_pck(self,pck_RREQ):
        pck_RREP = package(Network_layer._id_pck,'RREP',"i am a RREP",self.host.get_mac(),pck_RREQ.get_originator())
        
        logging.info(f' I am host[{self.host.get_mac()}] and received a RREQ pack from host[{pck_RREQ.get_originator()}]')
        logging.info(f' Host[{self.host.get_mac()}] is sending a RREP to host[{pck_RREQ.get_originator()}]')
        
        print(f'\033[36m --- HOST[{self.host.get_mac()}] is sending a RREP to HOST[{pck_RREQ.get_originator()}] ---\033[37m')
        Network_layer._id_pck += 1
        
        # get the way back
        way_back = pck_RREQ.get_path()
        for way in way_back:
            # save the way that pck has being through
            pck_RREP.add_path(way)
        
        # saving route
        self.table.save_route(way_back, pck_RREQ.get_originator())
        way_back.reverse()

        # The next jump is who sent to me
        next = way_back.pop(1)
        pck_RREP.add_next(next.get_mac())
        
        #than send to link layer
        self.host.link.sending_request(pck_RREP) 


    # Function to processe all packages received
    def receive_pck(self,pck):
        actual_mac = self.host.get_mac()
        
        if pck.get_type() == 'DATA':  
            # final point gets the package              
            if pck.get_destination() == self.host.get_mac():
                if self.add_received_pck(pck.get_id()):
                    print('\033[33m *'*28)
                    print(f'* I AM HOST[{self.host.get_mac()}] AND RECEIVED THE PACKAGE [{pck.get_contents()}] *')
                    print(' *'*28, '\033[37m')

                    logging.info(f' **** Host[{actual_mac}] received a pack from host[{pck.get_originator()}], message is [{pck.get_contents()}] ****')
                else:
                    pass
            #print for debugging
            print(f'\n\t \033[36m HOST[{actual_mac}] HAS PACK ? =======>{pck.get_next() == self.host.get_mac()} \033[37m')
            
            # the package is not for the actual host, it's on the path
            if (pck.get_destination() != self.host.get_mac() and pck.get_next() == self.host.get_mac()):
                print(f'\n \033[36m +++++ L3: HOST[{self.host.get_mac()}] RECIEVING A DATA PCK, BUT IS NOT MYNE -->[{pck.get_destination()}]\033[37m')
                logging.info(f'I am host[{actual_mac}] receiveing a data pack with id: {pck.get_id()}, but is not for me')
                
                if self.add_received_pck(pck.get_id()):
                    path = pck.get_path()
                    #print(f'THE PATH IS :{path}')
                    # get the next jump
                    next_jp = path.index(self.host)+1
                    next_jp = path[next_jp]
                    print(f'\033[36m NEXT POINT IS {next_jp.get_mac()}')
                    pck.add_next(next_jp.get_mac())

                    #then send the package
                    self.host.link.sending_request(pck)
                else:
                    pass
                

        if pck.get_type() == 'RREQ': # process request packages
            # if the request is for the actual host, then it must reply
            if pck.get_destination() == self.host.get_mac():
                if self.add_received_pck(pck.get_id()): # check if already have this pck 
                    pck.add_path(self.host)# add itself in the path
                        
                    # creates a reply package 
                    self.create_RREP_pck(pck)
                    # make a function or an attribute to add this new route
                else:
                    pass
                    
            else: # the request is not for the actual host
                if self.add_received_pck(pck.get_id()):
                    # ** verify the route table ** (still in progress)
                    # if has no way, just make a broadcast
                    logging.info(f' I am host[{actual_mac}] receiving a RREQ id:[{pck.get_id()}], but I am not the destination')
                    logging.info(f' So I (host[{actual_mac}]) must make a broadcast sending to my nighbors')

                    pck.add_path(self.host)
                    self.host.link.sending_request(pck)
                
        
        if pck.get_type() == 'RREP':
            # checks if the actual host is the destination and still doesn't have this package
            if pck.get_destination() == self.host.get_mac() and self.add_received_pck(pck.get_id()):
                print(f"\n\033[36m +++++++++ L3: HOST[{self.host.get_mac()}] MUST SEND THE DATA PACKAGE \033[37m")
                
                logging.info(f" I am host[{actual_mac}] and received a RREP from host[{pck.get_originator()}]")
                logging.info(f" So I(host[{actual_mac}]) must send the data pack!")

                data_pck = self.pending_pck.pop(0) # remove the 1rs pck from remaining ones
                way_back = pck.get_path()
                
                # save the way that pck has being through
                for way in way_back:
                    data_pck.add_path(way)
                    print(f'\n\033[36m GOT MY REPLY AND THAT IS THE WAY =>{way.get_mac()}\033[37m')
                
                self.table.save_route(way_back, pck.get_originator()) # save into the host's route table
                #add next
                try:
                    next_jump = way_back.index(self.host)+1 # check the position of actual host
                except Exception as e:
                    # must find a way function
                    print(e)
                    
                print(f'MY DATA PACK PATH IS => {data_pck.get_path()}')
                next_jump = way_back[next_jump] #get the next jump
                logging.info(f' And the next jump is to host[{next_jump.get_mac()}]')
                data_pck.add_next(next_jump.get_mac())# add the next jump to the pck information
                #print(f'\nL3: NEXT POINT IS {next_jump.get_mac()}')
                
                #send data
                self.host.link.sending_request(data_pck)
            

            # the actual host is the next jump and is getting this pck for the 1rs time
            elif pck.get_next() == self.host.get_mac() and self.add_received_pck(pck.get_id()):
                logging.info(f' I am host[{actual_mac}], received a DATA pack, but is not for me')
                logging.info(f" So I(host[{actual_mac}]) must send to next point")
                way_back = pck.get_path()
                
                try:
                    next_jump = way_back.index(self.host)-1 # check the position of actual host
                except Exception as e:
                    # ** must find a way function **
                    print(e)
                    
                next_jump = way_back[next_jump] #get the next jump
                logging.info(f' And the next jump is to host[{next_jump.get_mac()}]')
                pck.add_next(next_jump.get_mac())# add the next jump to the pck information
                self.host.link.sending_request(pck)