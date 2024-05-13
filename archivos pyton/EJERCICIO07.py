print ("SEMANA NO. 11 EJERCICIO 1")
 n = int(input("INGRESE UN NUMERO > 0"))
if( n<=0 ):
 print ("ERRO EL DATO DEBE SER MAYOR QUE 0")
 #DEFINICION DE VARIABLES
 a = 0;
 b = 0;
 c = 0;
 i = 0;
resultado = ""

#STRING STR PARA 
if( n > 0 ):
 resultado = str(a)
 
 if( n > 1 ):
  resultado += ", " + str(b)

  while(i < n):
   c = a + b
   resultado += ", " + str(c)
   a = b
   b = c
   i = i + 1
 #print ("DENTRO CICLO:", RESULTADO)
  print (resultado)
else:
 print (resultado)

#SEGUNDO EJERCICIO
 print("SEMANA NO. 11: EJERCIO 2")

 n2 = int(input("INGRESE UN NUMERO > 0"))

if( n2<=0 ):
  print("DEBE SER MAYOR QUE 0")
 
  #INCISO A 
  resultadoA = 0
  for x in range(1, n2 +1):
   resultadoA += 1/x

   print("inciso A:", resultadoA)
   
   #INCISO B
  