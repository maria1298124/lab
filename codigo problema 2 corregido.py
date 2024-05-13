#Problema 2
                    
print("CALCULADORA DE PRECIO DE ENVIO")

transporte= str(input("Desea el envio en motocicleta o vehículo: "))

km= int(input("A cuantos kilimetros desea realizar el envio: "))

moto= 10
vehiculo= 20

if transporte=="moto":
    km>0 or km<5 
    mt1= km*3
    mt11= mt1+moto 
    print(f"El cobro final del envio es de {mt11: .2f}")

else:
    if transporte=="moto": 
        km>5 or km<10 
        mt2= km*2.50 
        mt22= mt2+moto 
        print(f"El cobro final del envio es de {mt22: .2f}")
    else:
        if transporte=="moto": 
            km>10 
            mt3= km*2
            mt33= mt2+moto 
            print(f"El cobro final del envio es de {mt33: .2f}")

#str sirve para convertir un numero a texto
            #print("EL TOTAL DE SU ENVIO ES: + str (cobroTotal)")

if transporte=="vehiculo":
    km>0 or km<5 
    mt1= km*6
    mt11= mt1+moto 
    print(f"El cobro final del envio es de {mt11: .2f}")

else:
    if transporte=="moto": 
        km>5 or km<10 
        mt2= km*2.50
        mt22= mt2+moto 
        print(f"El cobro final del envio es de {mt22: .2f}")
    else:
        if transporte=="moto": 
            km>10 
            mt3= km*2
            mt33= mt2+moto 
            print(f"El cobro final del envio es de")