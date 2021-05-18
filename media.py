import random
import math

#Calculates mean.
def media(X):
    return sum(X)/len(X)

#Calculates variance. 
def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x-mu)**2

    return acumulador / len(X)

#Calculates standard deviation.
def des_Estandar(X):
    return math.sqrt(varianza(X))

#This main method is just for testing. 

if __name__ == '__main__':
    
    valor = [random.randint(9,12) for i in range(20)]
    mu = media(valor)
    Var = varianza(valor)
    sigma = des_Estandar(valor) 
    print(f'Arreglo X: {valor}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Deviación estandar = {sigma}')