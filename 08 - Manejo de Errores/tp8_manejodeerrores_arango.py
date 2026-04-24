# Juan Santiago Arango - 54193

def validar_numero_int(mensaje):
  while True:
    numero = input(mensaje).strip()
    if numero.isdigit() and numero != "":
      return int(numero)
    else:
      print("Entrada inválida. Por favor, ingrese un número válido.")

# Programa 1

a = 10
b = input("Introduce un número: ") # Si el usuario introduce un valor no numérico, se producirá un error (ValueError)
result = a / b # Se produce un error si b es 0 (ZeroDivisionError), si no es un número válido (ValueError) y al ser b un string, se produce un error (TypeError) al intentar dividir un número por una cadena de texto
print(f"Resultado: {result}")

numbers = [1, 2, 3]
print(numbers[5]) # Se produce un error (IndexError) porque se intenta acceder a un índice que no existe en la lista

# Programa 2

a = 10
b = validar_numero_int("Introduce un número: ")
if b == 0:
  print("No se puede dividir por cero. Por favor, ingrese un número diferente de cero.")
else:
  result = a / b
  print(f"Resultado: {result}")

numbers = [1, 2, 3]
print(numbers[2])

# Programa 3

a = 10
try:
  b = int(input("Introduce un número: "))
  result = a / b
  print(f"Resultado: {result}")
except:
  print("Ocurrió un error. Por favor, intente nuevamente.")

# Programa 4

a = 10
try:
  b = int(input("Introduce un número: "))
  result = a / b
  print(f"Resultado: {result}")
except ZeroDivisionError:
  print("No se puede dividir por cero. Por favor, ingrese un número diferente de cero.")
except ValueError:
  print("Entrada inválida. Por favor, ingrese un número válido.")
except TypeError:
  print("Tipo de dato inválido. Por favor, ingrese un número válido.")

# Programa 5

a = 10
try:
  b = int(input("Introduce un número: "))
  result = a / b
except ZeroDivisionError:
  print("No se puede dividir por cero. Por favor, ingrese un número diferente de cero.")
except ValueError:
  print("Entrada inválida. Por favor, ingrese un número válido.")
except TypeError:
  print("Tipo de dato inválido. Por favor, ingrese un número válido.")
else:
  print(f"Resultado: {result}")
finally:
  print("Gracias por usar el programa. ¡Hasta luego!")

# Programa 6

try:
  numero = int(input("Introduce un número: "))
  print(f"El número introducido es: {numero}")
except ValueError:
  print("Entrada inválida. Por favor, ingrese un número válido.")
except Exception as e:
  print(f"Ocurrió un error inesperado: {e}")

# Programa 7

while True:
  try:
    numero = int(input("Introduce un número: "))
    print(f"El número introducido es: {numero}")
    break
  except ValueError:
    print("Entrada inválida. Por favor, ingrese un número válido.")
  except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")