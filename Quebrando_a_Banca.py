#v2.0

#e1 = input().split()
#e2 = input()

#casos de testes
e1 = ['6', '1']
e2 = '313487'

num = e2
for i in range(int(e1[1])):
	print(i)
	maior = 0
	for i in num:
		#lista vazia pra dps remover o indice
		li = []
		for j in num:
			li.append(j)
		print(li)
		
		#removendo o indice
		n=''
		li.remove(i)
		print(li)
		
		#comparação
		for k in li:
			n += k
		print(n)
		if int(n) > maior:
			maior = int(n)
	
	#salva o valor do primeiro loop		
	num = str(maior)
	
print(maior)
