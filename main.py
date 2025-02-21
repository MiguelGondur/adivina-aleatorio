#coding utf - 8
#adivina numero aleatorio
import random
print('programa para adivinar un numero aleatorio entre 1 y 100')

#Variables 
limite_inferior = 1
limite_superior = 100
numero_aleatorio = random.randint(limite_inferior,limite_superior)

conteo_intentos = 0
numero_usuario = 0

#Ciclo de control
while numero_usuario != numero_aleatorio:
    numero_usuario = int(input('ingrese un numero entre el 1 y 100: '))
    conteo_intentos += 1
    
  #validar que el dato este dentro del rango (1-100)
    if numero_usuario < limite_inferior or numero_usuario > limite_superior:
        print('el numero ', numero_usuario, 'debe estar entre', limite_inferior, 'y', limite_superior)
        continue

    if numero_usuario > numero_aleatorio :
         print('el numero ', numero_usuario,' es mayor a el numero aleatorio. Intente de nuevo' )
    
    elif numero_usuario < numero_aleatorio:
         print('el numero ', numero_usuario,' es menor a el numero aleatorio. Intente de nuevo' )
         
         

print('felicidades encontraste el numero secreto en:', conteo_intentos,'intentos')