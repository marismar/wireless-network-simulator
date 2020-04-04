from host import host
from link import link_layer
from package import package

class master:
	def  __init__(self, host):
		self.send_queue = [] #save all the hostesses
		self.host = host

	def send_permission(self):	#function to allow sending packge 
		if len(send_queue) > 0:
			sender_allowed = self.send_queue.pop(0) #pop the host that made the first request 
			self.sender_allowed.link.send_pck_physical() #send a package to the host, allowing it to send  

	def add_queue(self, host):	#function to receive request to send a package
		self.send_queue.append(host) #add into a list every host that wants to send any type of package