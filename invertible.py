#invertible: int -> int
# lo que hace esta funcion es invertir los numeros
# ejemplo: invertir(81) return 18
def invertir(n):
    decena = n//10
    unidad = n%10
    invertido = 10*unidad + decena
    return invertido
assert invertir(81) == 18
assert invertir(18) == 81

