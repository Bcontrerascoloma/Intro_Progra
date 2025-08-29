import random
#azar: None -> int
#retorna un numero al azar entre 1 y 10
# ej azar() -> 3
def azar():
    return (random.random()*9)+1
#test
test = azar()
assert 1<=test and test<=10

