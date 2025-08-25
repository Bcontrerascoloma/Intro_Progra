from calcPromedio import *

c1 = float(input("Nota C1: "))
c2 = float(input("Nota C2: "))
c3 = float(input("Nota C3: "))
pc = round(promedioControles(c1,c2,c3),1)
if pc >= 5.5:
    print("Te eximiste del examen con", pc, "Aprovaste el curso!!")
else:
    ne = float(input("Nota Examen: "))
    nf = round(notaFinal(pc,ne),1)
    if nf < 4.0:
        resultado = "reprovaste el curso :("
    if nf >3.6: 
        resultado = "Te fuiste a examen de 2da"
    else:
        resultado = "Aprovaste el curso!!"
    print("Resultado:",resultado)


