from host import host
from package import package
from link import link_layer
from physical import physical_layer
from table import routing_table

class network_layer:
	def __init__(self,host):
		self.host = host
		self.table = routing_table()

	def send_pck():	#to link layer
		pass

	def receive_pck(self,pck):	#receive a package from link layer
		if(pck.get_originator() == self.host.get_mac()) #if the receptor is the package originator
			return	#ignore the package
		if((pck.get_type() == 'RREP' or pck.get_type() == 'DATA') and pck.get_next() != self.host.get_mac()):
			return #ignore the package
		if(not self.add_received_pck(pck)):	#add the package to the received list and check
			return #ignore the package if it already in the list
		if(pck.get_type() == 'DATA' and pck.get_destination() = self.host.get_mac()): #if the receptor is the package destination
			pck.get_contents() #receive contents of the package
			#IMPORTANT: write it in a log file
		elif(pck.get_type() == 'DATA' and pck.get_destination() != self.host.get_mac()): #if the receptor is next at the route
			if(self.table.check_route(pck.get_destination())) #check if there is a route
				pck.add_next(self.table.get_next_to(pck.get_destination())):	#add next to the route
				self.host.link.sending_request(pck)				
			else:	#if there is not a route in routing table
				pck.add_next([]) #send a RREQ package to all neighbors
				self.create_RREQ_pck(pck)
		elif(pck.get_type() == 'RREQ' and pck.get_destination() != self.host.get_mac()): #if the host is not the destination


		elif(pck.get_type() == 'RREQ' and pck.get_destination() == self.host.get_mac()):


		elif(pck.get_type() == 'RREP' and pck.get_destination() != self.host.get_mac()):
			count = 0
			host_position = -1
			for obj in pck.get_path():	#check the host position in the path
				if(obj == self.host.get_mac()):	
					host_position = count #when it is found, save it
					break
				count += 1
			if(host_position < 0):	#if the receptor host is not in the path
				pck.add_next([]) #send a RREQ package to all neighbors
				self.create_RREQ_pck(pck)
			else:	#if the receptor is in the path
				if(host_position < len(pck.get_path())):




		elif(pck.get_type() == 'RREP' and pck.get_destination() == self.host.get_mac()):
			

	def add_received_pck(self,pck):
		pass