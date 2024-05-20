from colorama import Fore, Back, Style

# Devuelve un arreglo de 8x8 vacío, representando un tablero de ajedrez
def crear_tablero() -> list[list[str]]:
    board = [['  ' for _ in range(8)] for _ in range(8)]
    return board

# Convierte una posición en notación de ajedrez a índices de matriz, regresa una tupla
def posicion_a_indices(position:str) -> tuple[int, int]:
    col, row = position[0], position[1]
    return ord(col) - ord('a'), int(row) - 1

# Convierte índices de matriz a una posición en notación de ajedrez
def indices_a_posicion(indices) -> str:
    col, row = indices
    return chr(col + ord('a')) + str(row + 1)

# Verifica si la posición está dentro del tablero
def validar_posicion(position:str) -> bool:
    if len(position) != 2:
        return False
    col, row = position[0], position[1]
    return 'a' <= col <= 'h' and '1' <= row <= '8'

# Agrega piezas al tablero
def agregar_piezas(board:list[list[str]], num_pieces:int) -> None:
    
    piezas_validas = ['rey', 'reina', 'torre', 'alfil', 'caballo', 'peon', 'peón']
    colores_validos = ['blanco', 'negro']
    
    if num_pieces <= 0:
        print(Fore.RED + "El número de piezas a ingresar debe ser mayor a 0." + Fore.RESET)
        return
    
    if num_pieces > 64:
        print(Fore.RED + "El número de piezas a agregar excede el tamaño del tablero." + Fore.RESET)
        return
    
    for _ in range(num_pieces):
        while True:
            piece = input("Tipo de pieza (alfil, peón, caballo, torre, etc.): ").strip().lower()
            if piece not in piezas_validas:
                print(Fore.RED + "Tipo de pieza inválido. Inténtalo de nuevo." + Fore.RESET)
                continue           
            
            color = input("Color (Blanco o Negro): ").strip().lower()
            if color not in colores_validos:
                print(Fore.RED + "Color de pieza inválido. Inténtalo de nuevo." + Fore.RESET)
                continue 
            
            position = input("Posición (ejemplo: a1, e4, f8): ").strip().lower()
            if validar_posicion(position):
                x, y = posicion_a_indices(position)
                if board[y][x] == '  ':
                    board[y][x] = f"{piece},{color}"
                    print(Fore.LIGHTCYAN_EX + f"Pieza {piece} de color {color} agregada en la posición {position}" + Fore.RESET)
                    break
                else:
                    print(Fore.YELLOW + "Esa posición ya está ocupada. Inténtalo de nuevo." + Fore.RESET)
            else:
                print(Fore.RED + "Posición inválida. Inténtalo de nuevo." + Fore.RESET)
                
    print(Fore.LIGHTBLUE_EX + "Todas las piezas agregadas." + Fore.RESET)

def obtener_movimientos_caballo(position:str) -> list:
    # Define los movimientos posibles de un caballo
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    x, y = posicion_a_indices(position)
    possible_moves = []
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 8 and 0 <= new_y < 8:
            possible_moves.append((new_x, new_y))
    return possible_moves

def evaluate_knight_moves(board:list[list[str]], posicion_caballo:str) -> list:
    x, y = posicion_a_indices(posicion_caballo)
    knight_piece = board[y][x]
    _, knight_color = knight_piece.split(',')
    valid_moves = []
    for move in obtener_movimientos_caballo(posicion_caballo):
        new_x, new_y = move
        if board[new_y][new_x] == '  ':
            valid_moves.append((move, "casilla vacía"))
        else:
            piece, color = board[new_y][new_x].split(',')
            if color != knight_color:
                valid_moves.append((move, f"pieza enemiga: {piece}"))
    return valid_moves

def imprimir_tablero(board:list[list[str]]) -> None:
    
    # Diccionario de piezas de ajedrez en unicode
    piezas = {
        'rey,blanco': '\u2654',
        'reina,blanco': '\u2655',
        'torre,blanco': '\u2656',
        'alfil,blanco': '\u2657',
        'caballo,blanco': '\u2658',
        'peon,blanco': '\u2659',
        'peón,blanco': '\u2659',
        'rey,negro': '\u265A',
        'reina,negro': '\u265B',
        'torre,negro': '\u265C',
        'alfil,negro': '\u265D',
        'caballo,negro': '\u265E',
        'peon,negro': '\u265F',
        'peón,negro': '\u265F',
    }
    
    print('    ' + '   '.join(chr(ord('A') + i) for i in range(8)))  # Imprime las letras de las columnas
    print('  +' + '---+' * 8)  # Imprime el borde superior del tablero
    for i, row in enumerate(board):
        
        row = [piezas.get(pieza, ' ') for pieza in row]
        print(f"{i+1} | " + ' | '.join(row) + " |")  # Imprime las filas con las piezas
        print('  +' + '---+' * 8)  # Imprime el borde entre las filas

def main():
    # Inicializa el tablero
    board = crear_tablero()
    
    # Agrega piezas al tablero
    try:
        num_pieces = int(input("Número de piezas a agregar en el tablero: "))
        agregar_piezas(board, num_pieces)
    except ValueError:
        print(Fore.RED + "Ingresa un número válido." + Fore.RESET)
        main()
    
    while True:
        posicion_caballo = input("Posición del caballo a evaluar (ejemplo: a1, e4, f8): ").strip().lower()
        if validar_posicion(posicion_caballo):
            x, y = posicion_a_indices(posicion_caballo)
            if board[y][x] == '  ':
                color = input("Color del caballo (blanco o negro): ").strip().lower()
                board[y][x] = f"caballo,{color}"
                break
            else:
                print("Esa posición ya está ocupada por otra pieza. Inténtalo de nuevo.")
        else:
            print(Fore.RED + "Posición inválida. Inténtalo de nuevo." + Fore.RESET)
    
    valid_moves = evaluate_knight_moves(board, posicion_caballo)
    
    print("Movimientos válidos:")
    for move in valid_moves:
        pos = indices_a_posicion(move[0])
        print(f"{pos} - {move[1]}")
    
    print("Matriz del tablero:")
    imprimir_tablero(board)
    
if __name__ == "__main__":
    main()