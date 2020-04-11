import logging

class master:
	def  __init__(self, id):
		self.send_queue = [] #save all the hostesses
		self.id = id
		self.sender_allowed = 0

	#Function to allow sending packge 
	def send_permission(self):	
		if len(self.send_queue) > 0:
			self.sender_allowed = self.send_queue.pop(0) # pop the host that made the first request 
			
			print(f'MASTER: Host[{self.sender_allowed.get_mac()}] is allowed to start sending ...\n')
			logging.info(f' Master: Host[{self.sender_allowed.get_mac()}] is allowed to start sending\n')
			self.sender_allowed.link.send_pck_physical() #send a package to the host, allowing it to send  
		else :
			print('MASTER : ** There is no host in the queue for sending **')
			logging.info(" I am the Master and there is no host in the queue for sending \n")

	# Function to receive request to send a package
	def add_queue(self, host):
		
		logging.info(f' Master : the host[{host.get_mac()}] wants to send a package, has being added for permission\n')
		print(f'\nMASTER: The HOST[{host.get_mac()}] wants to send a package has being added\n')
		# add into a list every host that wants to send any type of package
		self.send_queue.append(host)

	def get_master_id(self):
		return self.id

	def get_all_requestes(self):
		return self.send_queue