#esThanos:: int -> bool
#devuelve True si n es un numero de thanos y False si no.
#esThanos(2453) == true
def esThanos(n, pos=1,impar=0,par=0):
    if n == 0: 
        return impar == par
    digito = n%10
    if pos%2 == 1:#impar
        impar = digito + impar
    else:
        par = par + digito
    return esThanos(n//10,pos +1, impar,par)
        
assert esThanos(2453)
assert not esThanos(12)

#numerosThanos: int -> none
def numerosThanos(k,n=1,encontrados=0):
    if encontrados == k:
        return
    if esThanos(n):
        print(n)
        numerosThanos(k,n+1,encontrados+1)
    else:
        numerosThanos(k,n+1, encontrados)
        
