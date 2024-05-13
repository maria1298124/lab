import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def adivinar_numero(self, numero):
        intento = int(input(f"{self.nombre}, adivina el número: "))
        if intento == numero:
            print(f"{self.nombre} ha acertado!")
            self.puntos += 1
            return True
        elif intento < numero:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")
        self.puntos == 0 
        return False

def jugar():
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")
    continuar_jugando = True

    while continuar_jugando:
        numero_secreto = random.randint(1, 100)
        print("\nNuevo juego iniciado. Adivinen el número secreto (entre 1 y 100)")

        jugador_actual = jugador1
        while True:
            if jugador_actual.adivinar_numero(numero_secreto):
                break
            jugador_actual = jugador2 if jugador_actual == jugador1 else jugador1

        print(f"\nPuntuación actual: {jugador1.nombre}: {jugador1.puntos}, {jugador2.nombre}: {jugador2.puntos}")

        continuar = input("\n¿Quieren jugar otra vez? (si/no): ")
        if continuar.lower() != 'si':
            continuar_jugando = False

    print("\n¡Fin del juego!")

if __name__ == "__main__":
    jugar()
