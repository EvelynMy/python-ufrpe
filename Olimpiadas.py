def Partition_ouro(A,p,r):
    x = A[str(r)]
    i = p-1
    for j in range(p, r):
        if A[str(j)].ouro > x.ouro:
            i = i+1
            A[str(i)], A[str(j)] = A[str(j)], A[str(i)]
        elif A[str(j)].ouro == x.ouro:
            if A[str(j)].prata > x.prata:
                i = i+1
                A[str(i)], A[str(j)] = A[str(j)], A[str(i)]
            elif A[str(j)].prata == x.prata:
                if A[str(j)].bronze > x.bronze:
                    i = i+1
                    A[str(i)], A[str(j)] = A[str(j)], A[str(i)]
                elif A[str(j)].bronze == x.bronze:
                    if A[str(j)].nome < x.nome:
                        i = i+1
                        A[str(i)], A[str(j)] = A[str(j)], A[str(i)]

    A[str(i+1)], A[str(r)] = A[str(r)], A[str(i+1)]
    return i + 1

def quick_sort_ouro(A,p,r):
    if p<r:
        q = Partition_ouro(A,p,r)
        quick_sort_ouro(A,p,q-1)
        quick_sort_ouro(A,q+1,r)

# -------------------------------------------------------------------------------------------------

class Pais():
    def __init__(self, nome, ouro=0, prata=0, bronze=0):
        self.nome = int(nome)
        self.ouro = ouro
        self.prata = prata
        self.bronze = bronze
        self.sort = False
    
    def __repr__(self):
        return str(self.nome)
    
    def __str__(self):
        return str(self.nome)
    
    def addOuro(self):
        self.ouro += 1
    
    def addPrata(self):
        self.prata += 1
    
    def addBronze(self):
        self.bronze += 1    

def programa():
    #paises
    paises = {}

    #config - numero de paises(N)[0]   numero de modalidades(M)[1]
    config = input().split()
    for i in range(1, int(config[0])+1):
        paises[str(i)] = Pais(str(i))
    

    for j in range(int(config[1])):
        ent = input().split()

        paises[ent[0]].addOuro()
        paises[ent[1]].addPrata()
        paises[ent[2]].addBronze()
   
    #ordenacao
    quick_sort_ouro(paises,1,len(paises))
    string = ''
    for i in range(1, len(paises)+1):
        if i is not len(paises):
            string += str(paises[str(i)]) + ' '
        else:
            string += str(paises[str(i)])
    print(string)

programa()

#lista = {'1': Pais(1,0,0,0), '2': Pais(2,0,0,0), '3': Pais(3,0,0,0)}

#quick_sort_ouro(lista,1,len(lista))
#print(lista)
