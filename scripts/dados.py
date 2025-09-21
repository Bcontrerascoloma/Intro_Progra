from random import randint
def mover(casilla):
    d1 = randint(1,6)
    d2 = randint(1,6)
    suma = d1 + d2 + casilla
    if suma>63:
        nuevaCasilla= 63 - (suma-63)
    else:
        nuevaCasilla= suma
    if nuevaCasilla == 63:
        return 63 
    elif nuevaCasilla %9 == 0:
        return (nuevaCasilla +9)
    else:
        return nuevaCasilla
def ct(casilla):
    nuevaCasilla = mover(casilla)
    if nuevaCasilla == 63:
        return 1
    else:
        return 1 + ct(nuevaCasilla)
