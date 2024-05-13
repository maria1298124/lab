valor = int(input("Ingrese un número:"))
romano= ""
if 1<=valor<=999:
    #SEPARAMOS PARA QUE LEA LAS CENTENAS, DECENAS Y UNIDADES
    centenas = valor//100
    decenas = valor%100//10
    unidades = valor%100%10

    #PARA IMPRIMIR QUE LEA CENTENAS, DECENAS Y UNIDADES DE MANERA TEXTUAL LITERAL
    print("centenas = " + str(centenas))
    print("decenas = " + str(decenas))
    print("unidades = " + str(unidades))
else:
    print("Error, número no válido")

# EN CASO DE QUE VARIABLE ROMANO SEA X SERA IGUAL A : "VALOR ESTABLECIDO"
match centenas:
    case 1: romano ="C"
    case 2: romano ="CC"
    case 3: romano = "CCC"
    case 4: romano = "CD"
    case 5: romano = "D"
    case 6: romano = "DC"
    case 7: romano = "DCC"
    case 8: romano = "DCCC"
    case 9: romano = "CM"


match decenas:
    case 1: romano += "X"
    case 2: romano += "XX"
    case 3: romano += "XXX"
    case 4: romano += "XL"
    case 5: romano += "L"
    case 6: romano += "LX"
    case 7: romano += "LXX"
    case 8: romano += "LXXX"
    case 9: romano += "XC"

match unidades:
    case 1: romano += "I"
    case 2: romano += "II"
    case 3: romano += "III"
    case 4: romano += "IV"
    case 5: romano += "V"
    case 6: romano += "VI"
    case 7: romano += "VII"
    case 8: romano += "VIII"
    case 9: romano += "IX"


print("El número romano es: " + romano)
    