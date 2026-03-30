# Programa 1

edad = int(input("Ingresa tu edad: "))

if edad > 18:
  print("Eres mayor de edad.")

# Programa 2

nota = float(input("Ingresa tu nota (0-10): "))

if nota >= 6:
  print("Aprobado")
else:
  print("Desaprobado")

# Programa 3

numero = int(input("Ingresa un número par: "))

if numero % 2 == 0:
  print("Ha ingresado un número par")
else:
  print("Por favor, ingrese un número par")

# Programa 4

edad = int(input("Ingresa tu edad: "))
categoria = ""

if edad < 12:
  categoria = "Niño/a"
elif 12 <= edad < 18:
  categoria = "Adolescente"
elif 18 <= edad < 30:
  categoria = "Adulto/a joven"
else:
  categoria = "Adulto/a"

print(f"Tu categoría es: {categoria}")

# Programa 5

contrasena = input("Ingresa una contraseña: ")

if 8 <= len(contrasena) <= 14:
  print("Ha ingresado una contraseña correcta")
else:
  print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Programa 6

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if (media > mediana) and (mediana > moda):
  print("Se trata de sesgo positivo o a la derecha")
elif (media < mediana) and (mediana < moda):
  print("Se trata de sesgo negativo o a la izquierda")
elif media == mediana == moda:
  print("Se trata de distribución sin sesgo")
else:
  print("No se puede determinar el sesgo")

# Programa 7

texto = input("Ingresa una frase o palabra: ")
vocales = "aeiou"

ultima_letra = texto[-1].lower()

if ultima_letra in vocales:
  print(f"{texto}!")
else:
  print(texto)

# Programa 8

nombre = input("Ingresa tu nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = int(input("Selecciona una opción: "))

match opcion:
  case 1:
    print(nombre.upper())
  case 2:
    print(nombre.lower())
  case 3:
    print(nombre.title())
  case _:
    print("Opción no válida")

# Programa 9

magnitud = float(input("Ingresa la magnitud del terremoto en la escala de Richter: "))
categoria = ""

if magnitud < 3:
  categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
  categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
  categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
  categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
  categoria = "Muy fuerte (puede causar daños significativos)"
elif magnitud >= 7:
  categoria = "Extremo (puede causar graves daños a gran escala)"

print(f"El sismo se categoriza: {categoria}")

# Programa 10

hemisferio = input("Ingresa el hemisferio en el que te encuentras (N/S): ").strip().lower()
mes = int(input("Ingresa el mes actual: "))
dia = int(input("Ingresa el día del mes: "))

if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
  if hemisferio == "n":
    estacion = "Invierno"
  elif hemisferio == "s":
    estacion = "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
  if hemisferio == "n":
    estacion = "Primavera"
  elif hemisferio == "s":
    estacion = "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
  if hemisferio == "n":
    estacion = "Verano"
  elif hemisferio == "s":
    estacion = "Invierno"
else:
  if hemisferio == "n":
    estacion = "Otoño"
  elif hemisferio == "s":
    estacion = "Primavera"
  
print(f"La estación es: {estacion}")