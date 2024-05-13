import time

def contar_segundos(segundos):
    for i in range(segundos):
        print(f"Segundos transcurridos: {i+1}")
        time.sleep(1)

if __name__ == "__main__":
    segundos = int(input("Ingrese la cantidad de segundos a contar: "))
    contar_segundos(segundos)


import time

def contar_minutos(minutos):
    segundos_totales = minutos * 60
    for i in range(segundos_totales):
        minutos_transcurridos = i // 60
        segundos_restantes = segundos_totales - i
        print(f"Minutos transcurridos: {minutos_transcurridos}, Segundos restantes: {segundos_restantes}")
        time.sleep(1)

if __name__ == "__main__":
    minutos = int(input("Ingrese la cantidad de minutos a contar: "))
    contar_minutos(minutos)
