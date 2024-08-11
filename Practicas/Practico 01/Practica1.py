import random
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
def GenerarDatos(prompesos):
    datos: dict[float:float]
    datos = {}
    altura : float
    peso : float
    random.seed(5)
    for i in range(100):
        altura = random.randint(15000,20000)/100
        peso = random.randint(185, 249)/10 *(altura/100)**2
        prompesos[0] += peso
        datos[altura] = peso
    #print(datos)
    return datos
def ordenarDatos(diccionario:dict,listAlt):
    listPes :list
    listPes = []
    for i in range(len(diccionario)):
        listPes.append(diccionario[listAlt[i]])
    return listPes




#listas de datos
list_alturas : list
list_pesos :list
list_alturas = []
list_pesos = []


PromPesos: list
PromPesos = [0]
tabla = GenerarDatos(PromPesos)
list_alturas = sorted(tabla)
PromPesos[0] /= 100

resta: float
sumErrores: float
ErrorMin : float
balance : list[int]
listVariables :list[float]

listVariables = [0,0]

ErrorMin = 999999
list_pesos = ordenarDatos(tabla,list_alturas)
plt.scatter(list_alturas, list_pesos)


# archivo excel
archivo = pd.DataFrame({'Alturas':list_alturas,'Pesos':list_pesos})
archivo.to_excel("Datos_Altura_peso.xlsx", index=False)

for i in range(-1000,1000):
    for j in range(-1000,1000):
        sumErrores = 0
        for d in range(len(list_alturas)):
            resta = abs(list_pesos[d] - (list_alturas[d]*j/100 +i/100))
            sumErrores += resta
        sumErrores = sumErrores/100
        if ErrorMin > sumErrores:
            ErrorMin = sumErrores
            listVariables = [i/100,j/100]
            """print(i,j)
            print(ErrorMin)"""
        
print("Acabo la Ejecucion")       
print(listVariables)

m = listVariables[1]
b = listVariables[0]


x = np.linspace(150, 210, 100)
y = m * x + b
plt.plot(x, y, label=f'y = {m}x + {b}')