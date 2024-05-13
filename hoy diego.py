monto_compra = int(input("Ingrese el monto de compra realizado: "))
if monto_compra<0:
    print("Monto invalido")
else:
 if monto_compra < 400:
    descuento = 0
    monto_final = monto_compra
 elif 400 <= monto_compra < 1000:
    descuento = 0.07
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
 elif 1000 <= monto_compra < 5000:
    descuento = 0.10
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
 elif 5000 <= monto_compra < 15000:
    descuento = 0.15
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
 else:
    descuento = 0.25
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento

print(f"El monto final de la compra es: Q{monto_final:.2f}")

#DIEGO ROSALES Y MARIA SANCHEZ 