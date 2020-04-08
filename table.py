from host import host
from package import package
from link import link_layer
from physical import physical_layer
from network import network_layer
from master import master

class routing_table:
	def __init__(self,host):
		self.host = host
		self.saved_routes = [] 
		self.routing = {}	#destination:next
		self.latest_search = []	#save the last search destination:next
		
	def check_route(self,destination):	#check if there is a route 
		for obj in self.routing:	
			if(obj == destination): #save the destination and next host as latest search
				self.latest_search[0] = destination
				self.latest_search[1] = self.routing[obj]
				return True
		return False	#if there is no route to the destination, return false

	def get_next_to(self,destination):	#get next host to the destination
		if(latest_search[0] == destination):
			return latest_search[1]
		else:
			return []		

	def save_route(self,path):	#save the all path to the destination 
		if(not path in self.saved_routes):	#check if there is already a saved route to the destination
			self.saved_routes.append(path) #if there is no route, save it
		iterator = path.index(self.host.get_mac()) #get the index of the host in path
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
		is_neighbor = True 	#the node is neighbor of the host
		path.reverse()	#reverse the path to save it
		iterator = path.index(self.host.get_mac())	#get the index of the host in path
		for obj in range(iterator,len(path)):
			if(is_neighbor):	#if is_neighbor is true 
				if(self.host.get_mac() != path[obj]):	#if the node in path is not the host
					self.routing[path[obj]] = path[obj]	#save node:node as destination:next
					neighbor_mac = path[obj]
					is_neighbor = False 	#the node is not neighbor of the host
			else:	#if the node in path is the host
				self.routing[path[obj]] = neighbor_mac	#save node:neighbor as destination:next 