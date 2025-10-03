import estructura
from lista import *
#Un arbol binario es una estructura recursiva o bien es vacia o vien contiene un valor y referencias de izq y derecha
#AB: valor(any), izq(AB), der(AB)
estructura.crear("AB", "valor izq der")
raiz = AB("F", AB("A",AB("G",None,None),AB("B",None,None)), AB("C",AB("D",None,None),AB("E",None,None)))

#valores: AB -> int
#cuenta el numero de elementos en un arbol
#ej: valores(raiz) devuelve 7

def valores(A):
    if A == None:
        return 0
    return 1 + valores(A.izq) + valores(A.der)
assert valores(raiz) == 7

#altura: AB -> int
#calcula la altura de un arbol binario
#ej: altura(raiz) devuelve 3
def altura(A):
    if A == None
        return 0 
    return 1 + max(altura(A.izq),altura(A.der))
assert altura(raiz) == 3

#ABB es un arbol binario tq:
# AB izq son menores que la raiz 
# AB der son mayores que la raiz
# AB der y AB izq son ABB
def esABB(A):
    if A == None: return True
    v = A.valor
    p = (A.izq==None) or mayor(A.izq) < v and esABB(A.izq)
    q = (A.der==None) or menor(A.der) > v and esABB(A.der)
    return p and q
assert esABB(raiz)

#mayor: AB -> any
#devuelve el valor mayor de un ABB
#ej: mayor(raiz) devuelve "G"
def mayor(A):
    if A.der == None: return A.valor
    return mayor(A.der)
assert mayor(raiz) == "G"

#menor: AB -> any
#devuelve el valor menor de un ABB
#ej: menor(raiz) devuelve "A"

def menor(A):
    if A.izq == None: return A.valor
    return menor(A.izq)
assert menor(raiz) == "A"


#enABB: any AB -> bool
#determina si un elemento esta o no en un ABB
#ej: enABB("E",raiz) devuelve True
def enABB(x,A):
    if A == None: return False
    if x < A.valor: return enABB(x,A.izq)
    if x > A.valor: return enABB(x,A.der)
    return True
assert enABB("E",raiz)
assert not enABB("K",raiz)

#insertar: any AB -> AB
#devuelve un nuevo ABB insertando x en el ABB A
#ej: insertar("A",AB("B",None,None)) devuelve
# AB("B",AB("A",None,None),None)
def insertar(x,A):
    if A==None: return AB(x,None,None)
    v = A.valor
    if x <= v: return AB(v, insertar(x,A.izq), A.der)
    if x > v: return AB(v, A.izq, insertar(x,A.der))
assert insertar("A",AB("B",None,None))== AB("B",AB("A",None,None),None)

