from package import package
from network import Network_layer
import logging

class link_layer:
	def __init__(self,host):
		self.host = host
		self.pending_pck = []
		self.package = 0

	def receive_pck_physical(self,pck):	#receive a package from physical layer
		self.host.network.receive_pck(pck)	#send the package to network layer

	def sending_request(self,pck):
		self.pending_pck.append(pck)	#add the package to pending list
		print(f'\n \033[33m +++++++ L2: List of package in link_layer :{self.pending_pck} \033[37m \n')
		logging.info(f' Sending a request to Master from host[{self.host.get_mac()}]')
		self.host.master.add_queue(self.host)	#host gets in the master queue

	def send_pck_physical(self): #send a package to physical layer
	 	self.package = self.pending_pck.pop(0)
	 	print(f'\033[33m +++++++ L2: LINK_LAYER OF HOST[{self.host.get_mac()}]\033[37m \n')
	 	self.package.package_info()
	 	self.host.physical.send_pck(self.package) 