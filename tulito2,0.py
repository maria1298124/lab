print ("Ejercicio 2")

num = int(input("Ingrese un numero para multiplicar\n"))
speed= int(input("ingrese la velocidad (de cuanto a cuanto se multiplicas ) \n"))
ni = int(input("Ingrese desde que numero quiere que inicie la multiplicacion\n"))
nf = int(input("Ingrese desde que numero quiere que termine la multiplicacion\n"))
if nf<ni:
        print("El rango no es valido")
else:
    while ni<=nf:
        print(str(num), "x", str(ni), "=", str(num * ni) )
        if ni==1:
             ni=speed
        else:
            ni=ni+speed