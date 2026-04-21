# Juan Santiago Arango - 54193

def validar_numero_int(mensaje):
  while True:
    numero = input(mensaje).strip()
    if numero.isdigit() and numero != "":
      return int(numero)
    else:
      print("Entrada inválida. Por favor, ingrese un número válido.")

def validar_numero_float(mensaje):
  while True:
    numero = input(mensaje).strip()
    if numero.replace('.', '', 1).isdigit() and numero != "":
      return float(numero)
    else:
      print("Entrada inválida. Por favor, ingrese un número válido.")

# Programa 1

def imprimir_hola_mundo():
  print("Hola Mundo!")

imprimir_hola_mundo()

# Programa 2

def saludar_usuario(nombre):
  print(f"Hola {nombre}!")

saludar_usuario("Marcos")

# Programa 3

def informacion_personal(nombre, apellido, edad, residencia):
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = validar_numero_int("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# Programa 4

import math

def calcular_area_circulo(radio):
  return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
  return 2 * math.pi * radio

radio = validar_numero_float("Ingrese el radio del círculo: ")
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# Programa 5

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = validar_numero_float("Ingrese el número de segundos: ")
horas = segundos_a_horas(segundos)
print(f"{segundos:.2f} segundos equivalen a {horas:.2f} horas.")

# Programa 6

def tabla_multiplicar(numero):
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

numero = validar_numero_int("Ingrese un número para mostrar su tabla de multiplicar: ")
tabla_multiplicar(numero)

# Programa 7

def operaciones_basicas(a, b):
  suma = a + b
  resta = a - b
  multiplicacion = a * b
  division = a / b if b != 0 else "No se puede dividir por cero"
  
  return suma, resta, multiplicacion, division

numero = validar_numero_float("Ingrese el primer número: ")
numero2 = validar_numero_float("Ingrese el segundo número: ")
resultados = operaciones_basicas(numero, numero2)
print(f"Suma: {resultados[0]:.2f}")
print(f"Resta: {resultados[1]:.2f}")
print(f"Multiplicación: {resultados[2]:.2f}")
print(f"División: {resultados[3] if numero2 == 0 else f'{resultados[3]:.2f}'}")

# Programa 8

def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  return imc

peso = validar_numero_float("Ingrese su peso en kg: ")
altura = validar_numero_float("Ingrese su altura en metros: ")
imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

# Programa 9

def celsius_a_fahrenheit(celsius):
  return (celsius * (9/5)) + 32

celsius = validar_numero_float("Ingrese la temperatura en Celsius para transformarla a Fahrenheit: ")
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}")

# Programa 10

def calcular_promedio(a, b, c):
  return (a + b + c) / 3

num1 = validar_numero_float("Ingrese el primer número: ")
num2 = validar_numero_float("Ingrese el segundo número: ")
num3 = validar_numero_float("Ingrese el tercer número: ")
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los números es: {promedio:.2f}")