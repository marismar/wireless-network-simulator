from physical import physical_layer
from link import link_layer
from network import network_layer
from package import package
from table import routing_table
import weakref
import math

class host:

	_instances = set()	#atribute protect to save all instances of host

	def __init__(self, mac, x, y, master, reach):	#delfaut constructor
		self.physical = physical_layer(self)
		self.link = link_layer(self)
		self.network = network_layer(self)
		self.master = master
		self.reach = reach
		self.mac = mac
		self.positionx = x
		self.positiony = y
		self._instances.add(weakref.ref(self))	

	@classmethod	#to list all instances of host class
	def get_instances(cls):
		dead = set()
		for ref in cls._instances:
			obj = ref()
			if obj is not None:
				yield obj
			else:
				dead.add(ref)
		cls._instances -= dead

	def send_message(self,message,destination):	#send the package to network layer
		if(len(message) > 0 and len(destination) == 0):	#check if message is valid
			# pck = package(id,'DATA',path,message,self.mac,destination)	#new package with the message
			self.network_layer.send_pck()	

	def is_reacheable(self,neighbor):	#check if neighbor host is reacheable
		first_part = ((self.positionx - neighbor.positionx)**2)
		second_part = ((self.positiony - neighbor.positiony)**2)
		distance = math.sqrt(first_part + second_part)
		return distance <= self.reach #returns true if is reacheable

	def get_neighbors(self):	#get all neighbors of a host
		neighbors = []
		for obj in host.get_instances():
			if(self.is_reacheable(obj)):	#check if a node is reacheable
				neighbors.append(obj)	#add to the list of neighbors
		return neighbors #returns the list

	def get_mac(self):	#returns the mac address
		return self.mac 	

	def get_positionx(self):	#returns the first coordinate location
		return self.positionx

	def get_positiony(self):	#returns the second coordinate location
		return self.positiony

	def get_reach(self):	#returns the reach
		return self.reach