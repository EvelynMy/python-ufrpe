e1 = input().split()
e2 = input()

li = []
for i in e2:
	li.append(i)

for i in range(int(e1[1])):
	li.remove(min(li))
	#esse print mostra o "passo a passo"
	#print(li)
char =''
for i in li:
	char += i
print(char)