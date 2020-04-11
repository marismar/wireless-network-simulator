from host import host
from master import master
import matplotlib as plt
import logging
'''
def plot_host(host):
	ax = plt.subplot()
	nos, px, py = [], [], [] 
	n = ['h1', 'h2', 'h3', 'h4', 'h5']

	for obj in host:
		px.append(obj.get_positionx())
		py.append(obj.get_positiony())
		circle = plt.Circle((obj.get_positionx(), obj.get_positiony()), obj.get_reach(), color='red',fill=False)
		ax.add_patch(circle)

	for i, txt in enumerate(n):
		print(px[i])
		ax.annotate(txt, (px[i], py[i]))

	plt.plot(px, py, 'bo')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.title("Hostesses")#Muda título do gráfico
	plt.show()
	#plt.savefig('Plot_host.png')
'''
name = 'GUSSS'
logging.basicConfig(filename='test.log', level=logging.INFO) # testing log
logging.info('Hello world, this is %s', name)

# Creating master
m1 = master(id = 100)


# Creating hostesses
h1 = host(mac=1, x=1, y=0, master=m1, reach=4)
h2 = host(mac=2, x=2, y=3, master=m1, reach=4)
h3 = host(mac=3, x=3, y=5, master=m1, reach=4)
h4 = host(mac=4, x=15, y=10, master=m1, reach=4)
h5 = host(mac=10, x=5, y=7.5, master=m1, reach=4)
#h6 = host(mac=6, x=3, y=2, master=m1, reach=4)

#y = h1.get_instances()
#plot_host(y)

# ******** Starting the simulation ********
h1.send_message("hello friend 2", 3)
#h2.send_message("hello friend", 10)
#h3.send_message("hello friend", 1) # OK

# ------ Test with 2 points connected -----
#h1.send_message("hello friend", 3) # works OK
#h2.send_message("hello friend", 1) # works OK
#h3.send_message("hello friend", 1) # works OK

c =0
while m1.get_all_requestes() != []:
	print(f"***************** TIME {c} **************\n")
	if c == 9:
		break
	c+=1
	m1.send_permission()