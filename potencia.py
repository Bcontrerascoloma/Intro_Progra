#potencia(n) int->int
#calcula la potencia positiva de un entero
#ejemplo potencia(2,3) == 8
def potencia(x,y):
    if y == 0:
        return 1
    else:
        return x*potencia(x,y-1)


assert potencia(2,0)==1 
assert potencia(2,3)==8
