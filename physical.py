from package import package
from link import link_layer
import logging

class physical_layer:
	def __init__(self,host):
		self.host = host
		self.list_send = []

	def send_pck(self,pck):	#send a package to host
		neighbors = self.host.get_neighbors()	#get a list of all neighbors host

		for obj in neighbors:	#send the package in broadcast to all neighbors
			self.list_send.append(obj)#
			print(f'\033[32m IN PHYSICAL_LAYER , SENDING TO -> HOST[{self.host.get_mac()}] SENDING TO -> HOST[{obj.get_mac()}] \033[37m\n')
			
			logging.info(f' I am host[{self.host.get_mac()}], and I am sending a pack to neighbor[{obj.get_mac()}]')
			obj.physical.receive_pck(pck)	#each neighbor host receive the package


	def receive_pck(self,pck):	#receive a package from host
		self.host.link.receive_pck_physical(pck)	#send the package to link layer 