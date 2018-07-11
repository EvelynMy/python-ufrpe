ent = int(input())
soma = 0

for i in range(1, ent+1):
	soma += i
	
entrada2 = input()
li = entrada2.split()
dele = 0

for i in li:
	dele += int(i)

falta = soma - dele
print(falta)