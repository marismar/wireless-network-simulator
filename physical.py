from host import host
from package import package
from link import link_layer
from network import network_layer
from table import routing_table
from master import master


class physical_layer:
	def __init__(self,host):
		self.host = host

	def send_pck(self,pck):	#send a package to host
		neighbors = self.host.get_neighbors()	#get a list of all neighbors host
		for obj in neighbors:	#send the package in broadcast to all neighbors
			obj.physical.receive_pck(pck)	#each neighbor host receive the package

	def receive_pck(self,pck):	#receive a package from host
		self.host.link.receive_pck_physical(pck)	#send the package to link layer 