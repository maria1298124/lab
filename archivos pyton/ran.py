import random

def adivinar_numero():
   
    secreto = random.randint(1, 100)
    intentos = 0
    
    while True:
        try:
            
            Ingresado = int(input("Adivina el número (entre 1 y 100): "))
            puntos += 1
            if Ingresado == secreto:
                print("¡Felicidades! Has adivinado el número.")
                puntos += 1
                print("Tus puntos totales son:", puntos)
                break
            else:
                print("Ese no es el número. ¡Intenta de nuevo!")
                
                if Ingresado<secreto:
            print("EL NUMEOR INGRESADO ES MENOR")

        else:
 print("Numero es mayor")

                



adivinar_numero()



        