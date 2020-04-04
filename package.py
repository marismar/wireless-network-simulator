from host import host
from link import link_layer
from network import network_layer
from physical import physical_layer
from table import routing_table

class package:
	def __init__(self,id,type,path,contents,originator,destination):
		self.id = id
		self.type = type
		self.path = path	
		self.next = path[0]
		self.contents = contents
		self.originator = originator
		self.destination = destination

	def add_path(self,host):
	 	if(self.type == 'RREQ' or self.type == 'RREP'):
	 		self.path.append(host)

	def add_next(self,next):
		if(self.type == 'DATA' or self.type == 'RREP'):
			self.next = next	

	def get_type(self):	#returns the type
		return self.type

	def get_path(self):	#returns the path
		return self.path

	def get_contents(self):	#returns the contents
		return self.contents

	def get_originator(self):	#returns the originator
		return self.originator

	def get_destination(self):	#returns the destination
		return self.destination

