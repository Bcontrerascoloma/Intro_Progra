#Problema 1 
import estructura
from lista import *
#Persona:: nombre(str), nacimiento(int), padre(persona), madre(persona)

estructura.crear("persona" ,"nombre nacimiento padre madre")
#primera generacion ("abuelos")
carlos=persona("Carlos",1926, None, None)
beatriz=persona("Beatriz", 1926, None, None)

#segunda generacion ("padres")
andres = persona("Andres", 1950, carlos, beatriz)
david = persona("David", 1955, carlos, beatriz)
eva = persona("Eva", 1965, carlos,beatriz)
federico = persona("Federico", 1966, None, None)
#tercera generacion ("nietos")
gustavo = persona("Gustavo", 1996, federico, eva)

#esAncestro: persona persona -> bool 
# return True if the x person is ancestor of p person
# ej: esAncestro(carlos, gustavo) -> True 
def esAncestro(x,p):
    if p == None:
        return False
    if p.padre == None and p.madre == None:
        return False
    #comprobar si es ancestro por parte de padre es comprobar si x es padre de p o si x es ancestro de p.padre
    porpadre = (p.padre != None and p.padre == x) or esAncestro(x, p.padre)
    # por parte de madre es analogo

    pormadre = (p.madre != None and p.madre == x) or esAncestro(x, p.madre)
    return porpadre or pormadre
assert esAncestro(carlos , gustavo)

#ancestros:: persona -> lista(persona)
#lista con ancestros de la persona P
#ej: ancestros(david) es lista(carlos,lista(beatriz,listaVacia))
def ancestros(P):
    if P==None:
        return listaVacia
    if P.padre == None:
        L1 = listaVacia
    else:
        L1 = lista(P.padre,ancestros(P.padre))
    if P.madre == None:
        L2 = listaVacia
    else:
        L2 = lista(P.madre,ancestros(P.madre))
    return concatenar(L1,L2)
def concatenar(L1,L2):
    assert esLista(L1) and esLista(L2)
    if L2 == listaVacia:
        return L1
    elemento = cabeza(L2)
    if not enLista(elemento,L1):
        L1 = lista(elemento,L1)
    return concatenar(L1,cola(L2))

    
