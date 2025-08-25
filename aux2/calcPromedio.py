#promedioControles float float float -> float
# Calcula el promedio simple entre controles
# ejemplo promediocontroles(1.0,1.0,1.0) return 1
def promedioControles(c1,c2,c3):
    return (c1+c2+c3)/3
assert promedioControles(7.0,7.0,7.0) == 7.0
assert promedioControles(4.0,7.0,1.0) == 4.0

#notaFinal float float -> float
# clacula la nota final con un promedio de controles y un examen
# ej: notaFinal(4.0,4.0)->4.0
def notaFinal(promedio, examen):
    return 0.6*promedio+0.4*examen
assert notaFinal(4.0,4.0) == 4.0
