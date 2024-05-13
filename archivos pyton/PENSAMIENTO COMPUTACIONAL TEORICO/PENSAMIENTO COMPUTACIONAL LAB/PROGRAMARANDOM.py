import random

secreto = random.randint(1,100)
Ganador =  False
intentos = 0
while not Ganador:
    Ingresado = int(input("INGRESO UN NUMERO DEL 1 AL 100: "))
    intentos += 1
    if Ingresado == secreto:
        print("GANASTE!! FELICIDADES")
        Ganador = True
    else:
        print("VUELVE A INTENTAR")
        if Ingresado<secreto:
            print("EL NUMEOR INGRESADO ES MENOR")

        else:
            print("Numero es mayor")

            #quien gano y cuantos puntos le llevo al jugador que gano
              