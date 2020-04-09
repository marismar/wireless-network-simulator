#from host import host
#from link import link_layer
#from network import network_layer
#from physical import physical_layer
#from table import routing_table
#from master import master

class package:
	def __init__(self,id,type,contents,originator,destination):
		self.id = id
		self.type = type
		self.path = []	
		self.next = 0
		self.contents = contents
		self.originator = originator
		self.destination = destination

	def add_path(self,host): #add a host to the path
	 	if(self.type == 'RREQ' or self.type == 'RREP'):
	 		self.path.append(host)

	def add_next(self,next): #add a host as next
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

	def get_id(self):	#returns the id
		return self.id

	def get_next(self):
		return self.next

	def package_info(self):
		print('* '*24)
		print(f'* Package ID[{self.get_id()}] from HOST {self.get_originator()} to Destination:{self.get_destination()}  *')
		print(f'* Has contents :[{self.get_contents()}] AND Type: {self.get_type()} *')
		print('* '*24)