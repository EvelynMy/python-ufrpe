
loop = int(input())
casos = {}
for i in range(loop):
	cnt2 = 0
	ent = input().split()
	a = int(ent[0])
	b = int(ent[1])
	
	casoAnt = 0
	casoAnt_val = 0
	for n in range(a, b):
		
		if n%2 != 0:
			
			cnt = 0
			k = n
			
			while True:
				#print(k)
				if k == 3:
					cnt += 8
					break
				elif k == 2:
					cnt += 2
					break
				elif str(k) in casos:
					cnt = casos[str(k)] + cnt
					#print('entrou')
					break
				else:
					cnt += 1
					if k%2 != 0:
						k = 3*k+1
						cnt += 1
					k = int(k/2)
					
			casos[str(n)] = cnt
					
			#print('>>', n, cnt)
			if cnt > cnt2:
				cnt2 = cnt
				
				#print('CA', casoAnt, casoAnt_val)
	print('Caso %d: %d' %(i+1, cnt2))
	#print(casos)
	

