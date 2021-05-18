import random


def tirar_Dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range (numero_de_tiros):
        tiro = random.choice([1,2,3,4,5,6])
        tiro2 = random.choice([1,2,3,4,5,6])
        resultado = tiro + tiro2
        secuencia_de_tiros.append(resultado)

    return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_tiros = tirar_Dado(numero_de_tiros)
        tiros.append(secuencia_tiros)

    tiros_doce = 0

    for tiro in tiros:
        if 12 in tiro:
            tiros_doce += 1

    probabilidad_doce = tiros_doce/numero_de_intentos
    # probabilidad_uno = tiros_uno/numero_de_intentos

    print(f'La probabilidad de obtener por lo menos un doce en {numero_de_tiros} tiros es {probabilidad_doce}')

if __name__ == '__main__':
    numero_de_tiros = int(input('¿Cuántos tiros del dado?: '))
    numero_de_intentos = int(input('¿Cuántas veces quiere intentarlo? '))

    main(numero_de_tiros, numero_de_intentos)