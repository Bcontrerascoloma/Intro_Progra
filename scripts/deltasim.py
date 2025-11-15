
#diferenciaSimetrica
#entregra los elementos que solo estan en uno de los conjuntos 
# a = [1,2,3,4]
# b = [4,5,6,7]
#diferenciaSimetrica(a,b)==[1,2,3,5,6,7]
def diferenciaSimetrica(a,b):
    list= []
    for i in a:
        if i not in b:
            list.append(i)
    for i in b:
        if i not in list and i not in a:
            list.append(i)

    return list
a = [1,2,3,4]
b = [4,5,6,7]
assert diferenciaSimetrica(a,b) == [1,2,3,5,6,7]

