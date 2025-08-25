#factorial(n):: int -> int
#Entrega el factorial de n denotado n!
#ejemplo: factorial(4) == 24
def factorial(n):
    if n == 0: #Caso base
        return 1
    else:

        return n * factorial(n-1)
#test
assert factorial(0)==1
assert factorial(4)==24

