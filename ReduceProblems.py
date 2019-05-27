from functools import reduce

def SumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
    
    return resultado

def SumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor * 2
    
    return resultado

def ProductoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor
        
    return resultado

lista = [1, 3, -1, 15, 9]

sumatorio = reduce(lambda x, y: x + y, lista)
# creo una copia de la lista
l = lista [:] # con esta forma de copiar una lista no se cambia la original
# añado el neutro para la suma en la posición cero
l.insert(0, 0) # en la posición 0, inserta el valor 0
sumatorioDobles = reduce(lambda x, y: x + y*2, l)

print(sumatorio)
print(sumatorioDobles)