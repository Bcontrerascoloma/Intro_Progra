# mayor(a,b,c) int int int -> int
# toma 3 numeros enteros y te devuelve el mayor de ellos 
# ejemplo: mayor(5,9,1) devuelve 9

def mayor(a,b,c):
    if a>b:
        if a>c:           return a
        else:
            return c
    else: 
        if b>c:
            return b
        else: 
            return c 
    if a>b and a>c:
        return a 
    else:
        if b>c:
            return b
        else:
            return c
    ganador = a
    if b > ganador:
        ganador = b
    if c > ganador:
        ganador = c
    return ganador
    #test
assert mayor (5,9,1) == 9
assert mayor(7,7,7) == 7
assert mayor (1,2,5) == 5
assert mayor(8,2,4) == 8
assert mayor(9,5,1) == 9
assert mayor(5,1,9) == 9

