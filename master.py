from host import host
from link import link_layer
from package import package
from network import network_layer
from physical import physical_layer
from master import master

class master:
	def  __init__(self, host):
		self.send_queue = [] #save all the hostesses
		self.host = host

	def send_permission(self):	#function to allow sending packge 
		if len(send_queue) > 0:
			sender_allowed = self.send_queue.pop(0) # pop the host that made the first request 
			print(f'{sender_allowed.get_mac()} is sending package')
			self.sender_allowed.link.send_pck_physical() #send a package to the host, allowing it to send  

# Function to receive request to send a package
	def add_queue(self, host):
		# add into a list every host that wants to send any type of package
		print(f'{host.get_mac()} wants to send a package\n')
		self.send_queue.append(host)