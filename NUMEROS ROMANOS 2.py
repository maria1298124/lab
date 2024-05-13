#
def convertir_a_romano(numero):
    if (numero < 1 or numero > 999):
        print("Número fuera de rango")
    
    romanos = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
        500: 'D', 900: 'CM', 1000: 'M'
    }
    
    resultado = ''
    valores = sorted(romanos.keys(), reverse=True)
    
    for valor in valores:
        while numero >= valor:
            resultado += romanos[valor]
            numero -= valor
            
    return resultado

def main():
    numero = int(input("Ingrese un número entero del 1 al 999: "))
    print(f"El número romano equivalente es: {convertir_a_romano(numero)}")

if __name__ == "__main__":
    main()
