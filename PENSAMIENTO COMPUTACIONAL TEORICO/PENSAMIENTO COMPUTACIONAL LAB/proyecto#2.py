def imprimir_tablero(tablero):
    for fila in tablero:
        print("".join(fila))

def inicializar_tablero():
    # crear un tablero vacio
    tablero = [[" " for _ in range(10)] for _ in range(10)]

    for i in range(8):
        if (i==0):
            print("A B C D E F G H")
        for j in range(10):
            if (i + j) % 2 == 0:
                tablero[i][j] = "N"
            else:
                tablero[i][j] = " "

    return tablero
tablero = inicializar_tablero()
imprimir_tablero(tablero) 