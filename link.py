class link_layer:
	def __init__(self,host):
		self.host = host

	def receive_pck_physical(self,pck):	#receive a package from physical layer
		self.host.network.receive_pck(pck)	#send the package to network layer

	# def receive_pck_network(self):	#receive a package from network layer
	# def send_pck_physical(self): #send a package to physical layer
	# 	self.host.physical_layer.receive_pck(pck)
 