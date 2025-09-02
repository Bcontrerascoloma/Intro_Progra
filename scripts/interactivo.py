import triangulo
print('Calcular el area y perimetro de un triangulo')
l1 = float(input('ingrese el valor del lado 1: '))
l2 = float(input('ingrese el valor del lado 2: '))
l3 = float(input('ingrese el valor del lado 3: '))

print('El perimetro es ', triangulo.perimetro(l1,l2,l3))
print('El area es ', triangulo.area(l1,l2,l3))

