def a():
	return []

rt = 34
hi = {'hi':1273}
print(hi)
hi[13] = 123
hi[rt] = 456
print(hi)
print(13 in hi)

c = a()
c.append(4)
c.append(5)
c.append(4)
c.append([42, 5])
c.append([55, 5])
print(c)
print(len(c))

for obj in range(5,len(c)):
	print(c[obj])