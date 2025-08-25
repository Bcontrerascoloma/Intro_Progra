#cachipunzapata str -> str
#entrega siempre la jugada ganadora 
#ejemplo cachipunzapata("piedra") == papel
def cachipunzapata(jugada):
    if jugada == "papel":
        return "tijera"
    elif jugada == 'piedra':
        return "papel"
    elif jugada == 'tijera':
        return "piedra"
#test
assert cachipunzapata("tijera") == "piedra"

