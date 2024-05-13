num = (input("Ingrese un Numero entre 1 - 999: "))
unidades=num%10
decenas=(num%100-num%10)//10
centenas=(num%1000-num%100)//100

if (num > 999 or <= 0):
print('Valor de centenas: ' + repr (centenas))
print('Valor de decenas: ' + repr (decenas))
print("Valor unidades: " + repr (unidades))
else:




