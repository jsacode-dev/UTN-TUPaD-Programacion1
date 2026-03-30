# Programa 1

print("Hola Mundo!")

# Programa 2

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# Programa 3

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar_residencia = input("Ingresa tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# Programa 4

import math

def calcular_area_circulo(radio):
  area = math.pi * radio ** 2
  return area

def calcular_perimetro_circulo(radio):
  perimetro = 2 * math.pi * radio
  return perimetro

radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# Programa 5

segundos = int(input("Ingresa el tiempo en segundos: "))
horas = segundos / 3600

print(f"El tiempo en horas es: {horas}")

# Programa 6

numero = int(input("Ingresa un número para calcular su tabla de multiplicar: "))

for i in range(1, 11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")

# Programa 7

num_1 = int(input("Ingresa el primer número: "))
if num_1 == 0:
  print("Error: Ingrese un número distinto de cero.")
  exit()

num_2 = int(input("Ingresa el segundo número: "))
if num_2 == 0:
  print("Error: Ingrese un número distinto de cero.")
  exit()

print(f"Suma: {num_1 + num_2}")
print(f"División: {num_1 / num_2}")
print(f"Multiplicación: {num_1 * num_2}")
print(f"Resta: {num_1 - num_2}")

# Programa 8

altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))

imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc}")

# Programa 9

temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
temperatura_fahrenheit = (9/5 * temperatura_celsius) + 32

print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}")

# Programa 10

n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

print(f"El promedio de los números es: {(n1 + n2 + n3) / 3}")