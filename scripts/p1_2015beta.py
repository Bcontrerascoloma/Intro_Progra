import estructura
from lista import *


estructura.crear("coeficiente","valor potencia")
P=lista(coeficiente(5,3),lista(coeficiente(3,1),None))

def evaluar(P,x):
    if P == None:
        return 0
    else:
        numero = cabeza(P)
        return numero.valor*(x)**numero.potencia + evaluar(cola(P),x)
assert evaluar(P,10) == 5030

def evaluarLista(P,L):
    assert esLista(P)
    assert esLista(L)

    if L == listaVacia:
        return None
    else:
        numero = cabeza(L)
        return lista(evaluar(P,numero),evaluarLista(P,cola(L)))
    assert evaluarLista(P,lista(10,lista(1,lista(2,None)))) == lista(5030,lista(8,lista(46,None)))
    
