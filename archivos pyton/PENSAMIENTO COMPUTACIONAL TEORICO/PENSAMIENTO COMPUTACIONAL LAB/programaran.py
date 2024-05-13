import random

secreto = random.randint(1,100)
Ganador =  False
while not Ganador:
    Ingresado = int(input("INGRESO UN NUMERO DEL 1 AL 100: "))
    if Ingresado == secreto:
        print("GANASTE!! FELICIDADES")
        Ganador = True
    else:
        print("VUELVE A INTENTAR")
        if Ingresado<secreto:
            print("EL NUMEOR INGRESADO ES MENOR")

        else:
            print("Numero es mayor")