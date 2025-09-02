import turtle
#Kock: int int -> none
# dibuja la curva de koch de largo size
# y largo minimo min_size
# ejemplo : koch (320 , 1)
def koch ( size , min_size ):
    if ( size / 3 < min_size ):
# caso base
        turtle . forward ( size )
    else :
# caso recursivo
        koch ( size / 3 , min_size )
        turtle . left (60)
        koch ( size / 3 , min_size )
        turtle . right (120)
        koch ( size / 3 , min_size )
        turtle . left (60)
        koch ( size / 3 , min_size )
# snowflake : int int -> None
# dibuja el copo de nieve de Koch
# de un triangulo de lado size
# y lado minimo min_size
# ejemplo : snowflake (320 , 1)
def snowflake ( size , min_size ):
    koch ( size , min_size )
    turtle . right (120)
    koch ( size , min_size )
    turtle . right (120)
    koch ( size , min_size )
# ejemplo de uso
turtle . speed (0)
snowflake (1000 , 5)
turtle . done ()
