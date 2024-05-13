
import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 10

    def adivinar_numero(self, numero):
        intento = int(input(f"{self.nombre}, adivina el número: "))
         
        if intento<numero:
            print("EL NUMEOR INGRESADO ES MENOR")

          else:
        print("EL NUMERO INGRESADO ES MAYOR")
            print("Numero es mayor")
        if intento == numero:
            print(f"¡{self.nombre} ha acertado!")
            self.puntos += 1
        else:
            print(f"Lo siento, {self.nombre} ha fallado.")
            self.puntos -= 1

def jugar():
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")
    continuar_jugando = True

    while continuar_jugando:
        numero_secreto = random.randint(1, 100)
        print("\nNuevo juego iniciado. Adivinen el número secreto (entre 1 y 100)")

        jugador1.adivinar_numero(numero_secreto)
        jugador2.adivinar_numero(numero_secreto)

        print(f"\nPuntuación actual: {jugador1.nombre}: {jugador1.puntos}, {jugador2.nombre}: {jugador2.puntos}")

        continuar = input("\n¿Quieren jugar otra vez? (s/n): ")
        if continuar.lower() != 's':
            continuar_jugando = False

    print("\n¡Fin del juego!")

if __name__ == "__main__":
    jugar()

