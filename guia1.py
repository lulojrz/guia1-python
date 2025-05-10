#ejercicio 1
import math
def imprimir_holaMundo():
   print("hola mundo")

def imprimir_verso():
  print("Estoy mirando atras\n y puedo ver mi vida entera \n y se que estoy en paz \n pues la vivi a mi manera")


def raiz_de2():
    print("la raiz cuadrada de 2 es: " ,  round(math.sqrt(2),4))


def factorial_de_2():
  print("factorial de 2 es " , math.factorial(2))

def perimetro():
  print("el perimetro de una circunferencia de radio 1 es : " , math.pi * 2)

#ejercicio 2

def imprimir_saludo(nombre):
  print("hola" , nombre)
  

def raiz_cuadrada(num):
  print("la raiz cuadrada de " , num , "es :" , math.sqrt(num))

def  fahrenheit_a_celsius (temp) :
  print("la temperatura convertida de fahrenheit a celsius es :" ,
       round((((temp-32)*5)/9),1)  )

def imprimir_dos_veces(estribillo):
  print(estribillo*2)


def es_multiplo_de(x,y):
  if (x % y ==0):
   print("son multiplos")
  else:
    print("no son multiplos")


def es_par(x):
  es_multiplo_de(x,2)


def cantidad_de_pizzas(comensales,minimoxpersona) :
   total_porciones = comensales*minimoxpersona
   print("se necesitan ", math.ceil(total_porciones / 8 ))

#ejercicio 3
def alguno_es_0(num1,num2):
  print(num1==0  or num2==0)

def ambos_son_0(num1,num2):
  print(num1==0 and num2 ==0)


def es_nombre_largo(nombre):
  print(len(nombre) > 3 and len(nombre) < 8 )


def año_bisiesto(año):
  print((año%400 == 0 ) or (año % 100 != 0 and año%4==0)  )

#ejercicio 4
def peso_pino(arbol):
  if (arbol< 300):
    return arbol*3
  else:
    
    calc = arbol - 300
    return (calc*2 )+ 900


def es_peso_util(peso): 
   return (peso > 400 and peso<1000)  


def sirve_pino(peso):
  return es_peso_util(peso_pino(peso))

#ejercicio 5

def devolver_el_doble_si_es_par(num):
  if(num%2==0):
    return num*2

  else:
    return num

def devolver_valor_si_es_par_sino_el_que_sigue(num):
  if(num%2==0):
    return num
  else:
    return num+1



def lindo_nombre(nombre):
   if(len(nombre)<5):
     print("tu nombre es corto")
   else:
     print("tu nombre es largo")


def elRango(num):
  if (num<5):
    print("menor a 5")
  elif (num > 10 and num<20):
    print("esta en el rango 10 y 20")
  else:
    print("mayor a 20")


def vacaciones_o_trabajo(sexo,edad):
  if (sexo=="Masculino"):
       if (edad<=18 or edad >=65):
         print("andate de vacaciones")
       else:
         print("vaya a trabajar")
  else :
    if (edad<=18 or  edad>=60):
       print("andate de vacaciones")
    else:
       print("vaya a trabajar")

#ejercicio 6

#i = 1
#while(i<=10):
#  print(i)
#  i+=1


#x = 10
#while(x<=40):
 # if(x%2==0):
  #  print(x)
   # x+=1
 # else:
  #  x+=1


#i = 1
#while(i<=10):
 #print("eco")
 #i+=1

def cuentaregresiva(num):
  while (num >=1):
    print(num)
    num-=1


def viaje_en_el_tiempo(añoActual,añoPasado):
  while añoActual>= añoPasado:
    print("esta en el año", añoActual)
    añoActual-=1


def viaje_en_el_tiempo_2(añoActual):
  año = -384
  while añoActual>= año:
    print("esta en el año", añoActual)
    añoActual-=20

#ejercicio 7
#for num in range(1,11,1):
# print(num)

#for num in range(10,41,1):
 #if(num%2==0):
  #print(num)

#for num in range(1,11,1):
 # print("eco")

#def despegue_2(num):
 #  for i in range(num,-1,-1):
  #    print(i)


#def viaje_en_el_tiempo2_for(añoActual,AñoDeseado):
 #  for num in range(añoActual,AñoDeseado-1,-1):
  #    print("estamos en el año" , num)
  

#def viaje_a_aristoteles(añoActual):
 #  for num in range(añoActual,383,-20):
  #    print("estamos en el año", num)

#ejercicio 8
#son pavadas

#ejercicio 9
 #def rt(x: int, g: int)-> int:
  #g = g + 1
  #return x + g
  
#g: int = 0
 #def ro(x: int)-> int:
 #global g
 #g = g + 1
 #return x + g

#1. si evaluamos 3 veces ro(1)
