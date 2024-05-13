#SE ESTABLECE UN PARAMETRO Y UNA VARIABLE
def convertir_a_romano(numero):
    if numero < 1 or numero > 999:
        return "Número fuera de rango"
    #SE ESTABLECEN LIMITES DE 1 A 999

# SE ESTABLECEN VALORES DE UNIDADES DECENAS Y CENTENAS
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


for i in range(1, 1000):
    print(f"{i}: {convertir_a_romano(i)}")
