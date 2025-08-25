from cuadratica import *
a = int(input("Ingrese coeficiente a: "))
b = int(input("Ingrese coeficiente b: "))
c = int(input("Ingrese coeficiente c: "))
x1 = sol1(a,b,c)
x2 = sol2(a,b,c)
print(f"""
Raíz 1: {x1}
Raíz 2: {x2}
""")
