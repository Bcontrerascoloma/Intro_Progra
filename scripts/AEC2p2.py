from abc import ABC
import abc
import estructura
from lista import *
estructura.crear("ab", "valor izq der")

def validar(A):
    assert type(A) == ab
    arbolVacio = None
    if A == arbolVacio:
        return False
    if A.valor != None and A.izq= None and A.der= None:
        return True
    if A.izq != None and A.der != None:
       if (A.der.valor== A.valor or A.izq.valor == A.valor) and (A.der.valor != A.izq.valor)
            return validar(A.izq) and validar(A.der)
        else:
            return False
#rivales:: AB -> lista(str)
def rivales(A):
    if A == None:
        return listaVacia
    if A.valor == A.izq.valor:
        return lista(A.der.valor, rivales(A.izq)
    if A.valor == A.der.valor:
        return listaVacia
