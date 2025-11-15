#menores list int -> int
#reciba una lista (de Python) y un valor y devuelva el número (cantidad) de elementos de la lista que son menores que el valor.
# menores([1,2,3,4,5,6],4) == 3
def menores(lista,valor):
    contador = 0
    for i in lista:
        if i < valor:
            contador +=1
    return contador
#print(menores([1,2,3,4,5,6],4))


def listaMenores(lista):
    retorno = []
    for i in lista:
        n = menores(lista,i)
        retorno.append(n)
    return retorno
#print(listaMenores([50,30,70,20]))

def listaOrdenada(lista):
    r =[]
    listaindices = listaMenores(lista)
    for i in lista:
        r.append(0)
    for i in range(len(lista)):
        indice =listaindices[i]
        r[indice] = lista[i]
        
                
        
    return r
print (listaOrdenada([50,30,70,20]))
#assert listaOrdenada([50,30,70,20]) == [20,30,50,70]