candidatos=['Gabriela','José','Rosa','Matias']

votos = []
for i in candidatos:
    p = 'votos de '+ i +' ?'
    v = int(input(p))
    votos.append(v)
suma = sum(votos)
porcentaje=[]
for i in range(len(candidatos)):
    porcen= 100*votos[i]/suma
    porcentaje.append([porcen,candidatos[i]])
porcentaje.sort()
porcentaje.reverse()
for lista in porcentaje:
    print (lista[1], lista[0])