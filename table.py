
class route_table :
	def __init__(self,host):
		self.host = host
		self.route = {}
		
	def save_route(self, path, destination):
		self.route[destination] = self.route.get(destination, path) # path is a list with the way
		#print(f'{self.route}')

	# check if the dict has key "host"
	def check_route(self, host):
		if host in self.route:
			return True
		else:
			return False

	def next_jump(self, mac, host):
		next_jp = 0
		njp =0
		for key in self.route:
			for i in key:
				if mac == i.get_mac():
					next_jp = key
					break
		try:
			njp = next_jp.index(host)+1
		except :
			return False

		njp = next_jp[njp]
		return njp.get_mac() # return the next jump point


	def get_route(self):
		return self.route # return a dictionary