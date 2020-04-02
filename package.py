class package:
	def __init__(self,id,type,path,contents,originator,destination):
		self.id = id
		self.type = type
		self.path = path	
		self.next = path[0]
		self.contents = contents
		self.originator = originator
		self.destination = destination 	

	def get_type(self):	#returns the type
		return self.type

	def get_contents(self):	#returns the contents
		return self.contents

	def get_originator(self):	#returns the originator
		return self.originator

	def get_destination(self):	#returns the destination
		return self.destination

