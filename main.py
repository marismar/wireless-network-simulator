from physical import physical_layer
from link import link_layer
from network import network_layer
from table import routing_table
from host import host
from package import package
from master import master

# Creating master
m1 = master(id = 100)

# Creating hostesses
h1 = host(mac=1, x=1, y=0, master=m1, reach=4)
h2 = host(mac=2, x=1.8, y=3, master=m1, reach=4)
h3 = host(mac=3, x=2, y=2, master=m1, reach=4)
h4 = host(mac=4, x=5, y=3, master=m1, reach=4)
h5 = host(mac=10, x=9, y=1.9, master=m1, reach=4)

#y = h1.get_instances()

# ******** Starting the simulation ********
h1.send_message("hello friend", 2)

m1.send_permission()
#m1.send_permission()
#m1.send_permission()
#m1.send_permission()
#m1.send_permission()
#m1.send_permission()	

"""
ax = plt.subplot()
nos, px, py = [], [], [] 
num_de_no = int(input('Digite o números de nódulos da rede: '))
distancia = 1.5

for Id_do_no in range(1,num_de_no):
	x = random.randint(0,5)
	y = random.randint(0,5)
	nos.append(Nodulo(Id_do_no, x , y, 100))
	px.append(x)
	py.append(y)
	circle = plt.Circle((x, y), distancia, color='red',fill=False)
	ax.add_patch(circle)

plt.plot(px, py, 'bo')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Distribuição dos nós")#Muda título do gráfico
plt.show() #
plt.savefig('Mapa_dos_Nos.png')
"""