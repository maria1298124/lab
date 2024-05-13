#PROBLEMA: UN PROGRAMA QUE AL INGRESAR UN NUMERO ME DIGA SI ES PRIMO O NO 
numero = int(input("INGRESE UN NUMERO MAYOR QUE 1: "))
# PEDIR QUE INGRESE EL NUMERO Y QUE ESE NUMERO SEA IGUAL A LA VARIABLE NUMERO
contador = 0


if numero<=0 :
    print("ERROR NUMEOR INVALIDO")

else:
    for i in range(1, numero+1):
        if(numero%i==0):
            contador = contador+1
    if contador==2 or contador==1:
        print("EL NUMERO ES PRIMO")
    else:
        print("EL NUMERO NO ES PRIMO")