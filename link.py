#from host import host
from package import package
from network import network_layer
#from physical import physical_layer
from table import routing_table
#from master import master

class link_layer:
	def __init__(self,host):
		self.host = host
		self.pending_pck = []
		self.package = 0

	def receive_pck_physical(self,pck):	#receive a package from physical layer
		self.host.network.receive_pck(pck)	#send the package to network layer

	def sending_request(self,pck):
		self.pending_pck.append(pck)	#add the package to pending list
		print(f'\nList of package in link_layer :{self.pending_pck}\n')
		self.host.master.add_queue(self.host)	#host gets in the master queue

	def send_pck_physical(self): #send a package to physical layer
	 	self.package = self.pending_pck.pop(0)
	 	#print(f'IN LINK_LAYER :') # Working OK
	 	#package.package_info()
	 	self.host.physical.send_pck(self.package) 