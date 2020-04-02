import host
import package

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
			if(self.table.check_route(pck.get_destination())) 

			else:

		elif(pck.get_type() == 'RREQ' and pck.get_destination() != self.host.get_mac()): #if the host is not the destination


		elif(pck.get_type() == 'RREQ' and pck.get_destination() == self.host.get_mac()):


		elif(pck.get_type() == 'RREP' and pck.get_destination() != self.host.get_mac()):


		elif(pck.get_type() == 'RREP' and pck.get_destination() == self.host.get_mac()):
			

	def add_received_pck(self,pck):
		pass