
class routing_table:
	def __init__(self,host):
		self.host = host
		self.saved_routes = [] 
		self.routing = {}	#destination:next
		self.latest_search = []	#save the last search destination:next
		
	def check_route(self,destination):	#check if there is a route 
		print('\n ---------- T_L: I AM AT CHECK_ROUTE\n')
		print(f'----------- ROUTE DIC{self.routing}\n')
		
		for obj in self.routing:
			#save the destination and next host as latest search	
			if(obj == destination):
				print()
				self.latest_search[0] = destination
				self.latest_search[1] = self.routing[obj]
				return True
		return False	#if there is no route to the destination, return false

	def get_next_to(self,destination):	#get next host to the destination
		
		print(f"\n ---------- T_L: I AM AT GET_NEXT_TO ===== > {self.latest_search}")
		if(self.latest_search[0] == destination):
			return self.latest_search[1]
		else:
			return []		

	def save_route(self,path):	#save the all path to the destination 
		print('\033[33m \n ---------- T_L: I AM AT SAVE_ROUTE -----------------------------------\033[37m\n')
		
		if(not path in self.saved_routes):	#check if there is already a saved route to the destination
			self.saved_routes.append(path) #if there is no route, save it
		
		aux = self.saved_routes[0]
		print(f' \n ---------- T_L: {self.saved_routes} -----------------------------------\n')
		for i in aux:
			print(i.get_mac())

		print("\n--------------------- END PRINT --------------------------------------")
		
		# ORIGINALY -> iterator = path.index(self.host.get_mac())
		iterator = path.index(self.host) #get the index of the host in path
		print(f'\n ---------- T_L: ITERATOR IS ===== {iterator}\n')
		is_neighbor = True
		neighbor_mac = -1	#initiate a neighbor's mac address as -1(invalid) 
		
		for obj in range(iterator,len(path)):
			if (is_neighbor):	#if is_neighbor is true
				if(self.host.get_mac() != path[obj]):	#if the node in path is not the host
					self.routing[path[obj]] = path[obj]	#save node:node as destination:next
					neighbor_mac = path[obj]	
					is_neighbor = False 	#the node is not neighbor of the host
			else:	#if the node in path is the host
				self.routing[path[obj]] = neighbor_mac	#save node:neighbor as destination:next
		
		print(f'\n ---------- T_L: IS NEIGHBOR_MAC ===== {neighbor_mac.get_mac()}\n')
		'''
		is_neighbor = True 	#the node is neighbor of the host
		path.reverse()	#reverse the path to save it
		iterator = path.index(self.host)	#get the index of the host in path 

		for obj in range(iterator,len(path)):
			if(is_neighbor):	#if is_neighbor is true 
				if(self.host.get_mac() != path[obj]):	#if the node in path is not the host
					self.routing[path[obj]] = path[obj]	#save node:node as destination:next
					neighbor_mac = path[obj]
					is_neighbor = False 	#the node is not neighbor of the host
			else:	#if the node in path is the host
				self.routing[path[obj]] = neighbor_mac	#save node:neighbor as destination:next 
		'''
		print(f'\033[32m\n ---------- T_L: IS NEIGHBOR_MAC =====> {path}\n\033[37m')
		for i in path:
			print(f'\033[32m{i.get_mac()}\033[37m')
	
		print('\033[33m\n ---------- T_L: I AM AT SAVE_ROUTE END ----------------------------------\n\033[37m')


	def get_route(self):
		print(f' \n ---------- T_L: {self.saved_routes} -----------------------------------\n')
		aux = self.saved_routes[0]
		aux.reverse()
		
		#for i in aux:
		#	print(f'FROM TABLE.PY = {i.get_mac()}')
		return aux
