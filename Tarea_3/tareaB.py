#Clase Especie
#Especie:: nombre(str), ids(list[str]), avistamientos(list[str])
#Representa una especie de la reserva natural, almacena su nombre,
#los identificadores de los animales de esa especie y todos sus avistamientos.

class Especie:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ids = []
        self.avistamientos = []

    # Métodos de acceso
    def obtenerNombre(self):
        return self.nombre

    def obtenerIDs(self):
        return self.ids

    def obtenerAvistamientos(self):
        return self.avistamientos

    # Métodos de actualización
    def agregarID(self, ident):
        if ident not in self.ids:
            self.ids.append(ident)

    def agregarAvistamiento(self, avist):
        self.avistamientos.append(avist)


#VARIABLE DE ESTADO
#lista_especies:: list(Especie)
#Lista de objetos Especie presentes en el hábitat (vacía inicialmente)
lista_especies = []


#zonaMasProbable(especieAnimal, hora):: str, int -> str
#Dado el nombre de una especie y una hora (entera),
#retorna el puesto de observación más probable en que se observarán
#animales de dicha especie a esa hora.
#Ejemplo: zonaMasProbable("ciervo", 17) -> "Puesto7"

def zonaMasProbable(especieAnimal, hora):
    #buscar la especie en la variable de estado
    objeto = None
    for esp in lista_especies:
        if esp.nombre == especieAnimal:
            objeto = esp
            break

    if objeto is None:
        return "No hay datos suficientes"

    puestos = []

    for av in objeto.avistamientos:
        partes = av.split(" ")
        puesto = partes[0]
        horaAV = int(partes[2].split(":")[0])
        if horaAV == hora:
            puestos.append(puesto)

    if len(puestos) == 0:
        return "No hay datos suficientes"

    #calcular el más común
    mas_comun = puestos[0]
    max_rep = puestos.count(mas_comun)

    for p in puestos:
        rep = puestos.count(p)
        if rep > max_rep:
            max_rep = rep
            mas_comun = p

    return mas_comun


#agregarAvistamientos(nombreArchivo):: str -> None
#Dado el nombre de un archivo que contiene líneas del tipo:
#PuestoX,ID,AAAA-MM-DD,HH:MM
#agrega los avistamientos a los objetos Especie en la variable de estado.
#No elimina información previa.

def agregarAvistamientos(nombreArchivo):
    archivo = open(nombreArchivo, "r", encoding="utf-8")

    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            partes = linea.split(",")

            puesto = partes[0]
            ident  = partes[1]
            fecha  = partes[2]
            hora   = partes[3]

            avist = puesto + " " + fecha + " " + hora

            #buscar la especie a la que pertenece este ID
            especie_encontrada = None
            for especie in lista_especies:
                if ident in especie.obtenerIDs():
                    especie_encontrada = especie
                    break

            #si ya existe, se agrega el avistamiento
            if especie_encontrada is not None:
                especie_encontrada.agregarAvistamiento(avist)

    archivo.close()



#corregirHora():: None -> None
#Corrige todas las horas posteriores al 19-10-2025, ya que están
#adelantadas en 1 hora. Caso borde: si la hora era 00:MM,
#debe transformarse en 23:MM del día anterior.

def corregirHora():
    for especie in lista_especies:
        for i in range(len(especie.avistamientos)):
            
            av = especie.avistamientos[i]
            partes = av.split(" ")

            puesto = partes[0]
            fecha  = partes[1]
            hora   = partes[2]

            if fecha > "2025-10-19":

                hhmm = hora.split(":")
                h = int(hhmm[0])
                m = hhmm[1]

                h = h - 1

                if h < 0:
                    h = 23

                    partesFecha = fecha.split("-")
                    anio = int(partesFecha[0])
                    mes  = int(partesFecha[1])
                    dia  = int(partesFecha[2]) - 1

                    diasMes = [31,28,31,30,31,30,31,31,30,31,30,31]

                    if dia == 0:
                        mes = mes - 1
                        dia = diasMes[mes - 1]
                        if mes == 0:
                            mes = 12
                            anio = anio - 1

                    if mes < 10:
                        mesStr = "0" + str(mes)
                    else:
                        mesStr = str(mes)

                    if dia < 10:
                        diaStr = "0" + str(dia)
                    else:
                        diaStr = str(dia)

                    fecha = str(anio) + "-" + mesStr + "-" + diaStr

                if h < 10:
                    hStr = "0" + str(h)
                else:
                    hStr = str(h)

                nuevaHora = hStr + ":" + m

                especie.avistamientos[i] = puesto + " " + fecha + " " + nuevaHora
