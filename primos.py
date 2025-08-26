#primo: int -> bool
#retorna True si el numero dado (n>=2) es primo
#ej: primo(2) entrega True, primo(6) return False

# def es primo(n):
#     assert type(n) == int and n>=2
#     return esPrimo(n,2)
# assert primo(2)
# assert primo (13)
# assert not primo(6)


# #esPrimo: int (int) -> bool
# #devuelve True si entero n es primo probando desde 2
# #:ej: esPrimo(13) enrega True; primo(6) es False
# def esPrimo(n,divisor=2): 
#     assert type(n) == int and n >= 2 
#     if divisor == n: 
#         return True 
#     if n % divisor == 0: 
#         return False 
#     return esPrimo(n,divisor+1)
# assert esPrimo(13)
# assert not esPrimo(6)

#esPrimo: int -> bool
#devuelve True si entero n es primo 
#ej: esPrimo(13) enrega True; esPrimo(6) es False
def esPrimo(n):
    assert type(n) == int and n >=2
    if n == 2:
        return True
    if n%2 == 0:
        return False
    return esPrimoImpar(n)
assert esPrimo(13)
assert not esPrimo(6)

#esPrimo: int -> bool
#devuelve True si entero n es primo 
#ej: esPrimo(13) enrega True; esPrimo(6) es False
def esPrimoImpar(n,divisor=3):
    assert type(n) == int and n>=3 and n%2 ==1
    if divisor ** 2 >n:
        return True
    if n % divisor == 0:
        return False
    return esPrimoImpar(n,divisor+2)
assert esPrimoImpar(13)
assert not esPrimoImpar(9)
