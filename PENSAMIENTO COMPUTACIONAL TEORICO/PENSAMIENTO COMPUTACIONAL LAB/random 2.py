import random

def adivina_numero():
    
    numero_secreto = random.randint(1, 100)
    
    while True:
        try:
            
            guess = int(input("Adivina el número (entre 1 y 100): "))
            
        
            if guess == numero_secreto:
                print("¡Felicidades! Has adivinado el número.")
                break
            else:
                print("Ese no es el número. ¡Intenta de nuevo!")
        except ValueError:
            print("Por favor, ingresa un número válido.")


adivina_numero()
