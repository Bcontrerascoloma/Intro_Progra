#Problema 1 
import estructura
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
