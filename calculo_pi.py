import random
import math
from media import des_Estandar, media

def agujas(numero_de_agujas):
    ag_circulo = 0
    
    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])

        distancia_a_centro = math.sqrt(x**2 + y**2)

        if distancia_a_centro <= 1:
            ag_circulo += 1
        
    return ((4 * ag_circulo)/numero_de_agujas)

def estimacion(numero_de_agujas, num_intentos):
    estimados = []

    for _ in range(num_intentos):
        estimacion_pi = agujas(numero_de_agujas)
        estimados.append(estimacion_pi)
    
    media_estimados = media(estimados)
    sigma = des_Estandar(estimados)

    print(f'Estimados = {round(media_estimados,5)}, Desviación estándar = {round(sigma,5)}, Agujas = {numero_de_agujas}')

    return(media_estimados, sigma)

def estimar_pi(precision, num_intentos):
    numero_de_agujas = 1000
    sigma = precision

    while sigma >= precision/1.96:
        media,sigma = estimacion(numero_de_agujas, num_intentos)
        numero_de_agujas *= 2

    return media

if __name__ == '__main__':
    estimar_pi(0.1, 1000)