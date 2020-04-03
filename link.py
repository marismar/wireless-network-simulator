from host import host
from package import package
from network import network_layer
from physical import physical_layer
from table import routing_table

class link_layer:
	def __init__(self,host):
		self.host = host
		self.pending_pck = []

	def receive_pck_physical(self,pck):	#receive a package from physical layer
		self.host.network.receive_pck(pck)	#send the package to network layer

	def sending_request(self,pck):
		self.pending_pck.append(pck)	#add the package to pending list
		self.host.master.add_queue(self.host)	#host gets in the master queue

	def send_pck_physical(self): #send a package to physical layer
	 	self.host.physical_layer.receive_pck(pck) 