import estructura
#Complejo:: real(num) img(num)
estructura.crear("Complejo" ,"real img")
Comp1= Complejo(3, 0)
Comp2= Complejo(5, 2)
Comp3= Complejo(-4, -1)

def Re(z):
    return z.real

def Im(z):
    return z.img

def cartToStr(z):
    texto = (F"{z.real} + {z.img}i")
    return texto
assert cartToStr(Comp2) == "5 + 2i"

def mEscalar(z,r):
    return Complejo(r*Re(z),r*Im(z))
assert mEscalar(Comp3,2) == Complejo(-8,-2)

def suma(z1,z2):
    return Complejo(Re(z1)+Re(z2), Im(z1)+ Im(z2))
assert suma(Comp2, Comp3) == Complejo(1, 1)

def mult(z1,z2):
    re = (Re(z1)*Re(z2))-(Im(z1)*Im(z2))
    im = Im(z2)*Re(z1)+Im(z1)*Re(z2)
    return Complejo(re, im)
assert mult(Comp2,Comp3) == Complejo(18,-13)