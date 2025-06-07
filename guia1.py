
#ejercicio 1
import math
def imprimir_holaMundo():
   print("hola mundo")

def imprimir_verso():
  print("Estoy mirando atras\n y puedo ver mi vida entera \n y se que estoy en paz \n pues la vivi a mi manera")


def raiz_de2():
   return round(math.sqrt(2),4)


def factorial_de_2() -> float:
  return  math.factorial(2)

def perimetro()-> float:
  return  math.pi * 2

#ejercicio 2

def imprimir_saludo(nombre:str):
  print("hola" , nombre)
  

def raiz_cuadrada(num:int)->float:
  return  math.sqrt(num)

def  fahrenheit_a_celsius (temp:float)->float :
  
  return  round((((temp-32)*5)/9),1)  

def imprimir_dos_veces(estribillo:str):
  print(estribillo*2)


def es_multiplo_de(x:int,y:int)->bool:
    res = False
    if (y % x ==0):
     res = True

    return res


def es_par(x:int)->bool:
   return es_multiplo_de(2,x)


def cantidad_de_pizzas(comensales:int,minimoxpersona:int)->int :
   total_porciones = comensales*minimoxpersona
   return math.ceil(total_porciones / 8 )

#ejercicio 3
def alguno_es_0(num1:int,num2:int)-> bool:
   return num1==0  or num2==0

def ambos_son_0(num1:int,num2:int)->bool:
  return num1==0 and num2 ==0


def es_nombre_largo(nombre:str)->bool:
  return len(nombre) > 3 and len(nombre) < 8


def año_bisiesto(año:int)->bool:
  return (año%400 == 0 ) or (año % 100 != 0 and año%4==0)

#ejercicio 4
def peso_pino(arbol:int)-> int:
  if (arbol< 300):
    return arbol*3
  else:
    
   calc = arbol - 300
  return (calc*2 )+ 900


def es_peso_util(peso:int)->bool: 
   return (peso > 400 and peso<1000)  


def sirve_pino(peso:int)-> bool:
  return es_peso_util(peso_pino(peso))

#ejercicio 5

def devolver_el_doble_si_es_par(num:int)->int:
  if(num%2==0):
    return num*2

  else:
    return num

def devolver_valor_si_es_par_sino_el_que_sigue(num:int)->int:
  if(num%2==0):
    return num
  else:
    return num+1
  
def devolver_doble_simultiplode3_devolvertriple_simultiplode9(num:int)->int:
  if (num%3==0):
    return num*2
  elif (num%9==0):
    return num*3
  else:
    return num 
  
  



def lindo_nombre(nombre:str):
   if(len(nombre)<5):
     print("tu nombre es corto")
   else:
     print("tu nombre es largo")


def elRango(num:int):
  if (num<5):
    print("menor a 5")
  elif (num > 10 and num<20):
    print("esta en el rango 10 y 20")
  else:
    print("mayor a 20")


def vacaciones_o_trabajo(sexo:str,edad:int):
  if (sexo=="Masculino" or sexo =="masculino"):
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

def imprimir_num_1a10():
  i = 1
  while(i<=10):
   print(i)
   i+=1


def imprimir_pares_10a40():
 x = 10
 while(x<=40):
  if(x%2==0):
    print(x)
    x+=1
  else:
    x+=1

def imprimir_eco_10veces():
  
 i = 1
 while(i<=10):
  print("eco")
  i+=1

def cuentaregresiva(num:int):
  while (num >=1):
    print(num)
    num-=1


def viaje_en_el_tiempo(añoActual:int,añoPasado:int):
  while añoActual>= añoPasado:
    print("esta en el año", añoActual)
    añoActual-=1


def viaje_en_el_tiempo_2(añoActual:int):
  año = -384
  while añoActual>= año:
    print("esta en el año", añoActual)
    añoActual-=20

#ejercicio 7

def imprimir_num_1a10_for(num:int):
 for num in range(1,11,1):
  print(num)

def imprimir_pares_10a40_for(num:int):
  
 for num in range(10,41,1):
  if(num%2==0):
   print(num)


def imprimir_eco_10veces_for(num:int):
 for num in range(1,11,1):
   print("eco")

def despegue_2(num:int):
   for i in range(num,-1,-1):
      print(i)


def viaje_en_el_tiempo2_for(añoActual:int,AñoDeseado:int)-> str:
   for num in range(añoActual,AñoDeseado-1,-1):
      print("estamos en el año" , num)
  

def viaje_a_aristoteles(añoActual:int)-> str:
   for num in range(añoActual,383,-20):
      print("estamos en el año", num)

#ejercicio 8
#son pavadas

#ejercicio 9
def rt(x: int, g: int)-> int:
   g = g + 1
   return x + g
  

def ro(x: int)-> int:
  global g
  g = g + 1
  return x + g

#1. resultado si evaluamos 3 veces ro(1)? 
# # 2 + 3 + 4 = 9 
def ejecutar_3_veces()-> int:
 i=1
 resultado=0
 while (i<=3):
    resultado+=ro(1)
    i+=1

 return resultado   
resultado_imprimir = ejecutar_3_veces()
#2. resultado si evaluamos 3 veces rt(1,0)?
# 2+2+2
def evaluar_3_veces()-> int:
  i=1
  resultado = 0
  while(i<=3):
    resultado+= rt(1,0)
    i+=1

  return resultado


resultado_2 = evaluar_3_veces()  
