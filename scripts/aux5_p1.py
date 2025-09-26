from lista import *
#p1)
#jugador: nombre(str), puntaje(int), equipo(str)
estructura.crear("jugador", "nombre puntaje equipo")
j1 = jugador("juan",10,"rojo")

L1 = lista(jugador("juan",10,"rojo"), 
           lista(jugador("antonio",3,"azul"),
            lista(jugador("ana",7,"azul"),listaVacia)))
def jugadores_mayores_que(L,n):
    cabeza=cabeza(L)
    cola = cola(L)
    if esListaVacia(L):
        return 
    if cabeza.puntaje > n:
        return lista(cabeza,jugadores_mayores_que(cola(L),n))
    else:
        return jugadores_mayores_que(cola(L),n)
    
def jugadores_menores_que(L,n):
    cabeza=cabeza(L)
    cola = cola(L)
    if esListaVacia(L):
        return 
    if cabeza.puntaje < n:
        return lista(cabeza,jugadores_menores_que(cola(L),n))
    else:
        return jugadores_menores_que(cola(L),n)
def filtro(L,predicado):
    assert esLista(L)
    if L == listaVacia:
        return listaVacia
    if predicado(cabeza(L)):
        return lista(cabeza(L),filtro(cola(L),predicado))
    return filtro(cola(L),predicado)

def mapa(L,funcion):
    assert esLista(L)
    if L == listaVacia:
        return listaVacia
    y= funcion(cabeza(L))
    return lista(y, mapa(cola(L),funcion))

def reductor(L,operador,x):
    if cola(L) == listaVacia:
        return operador(x,cabeza(L)) #x: valor inicial
    return reductor(cola(L),operador,operador(x,cabeza(L)))

def optimq(L,n):
    return filtro(L,lambda x: x.puntaje>n)
def resetear_puntajes(L):
    return mapa(L,lambda x: jugador(x.nombre,0,x.equipo))

def puntaje_total(L):
    return reductor(L, lambda acc, y: acc+y.puntaje,0)
res = puntaje_total(L1)
print(res)