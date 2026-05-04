# Juan Santiago Arango - 54193

# Programa 1

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

while True:
  try:
    numero = int(input("Ingrese el tope máximo para el factorial (0 - 100): "))
    if numero >= 0 and numero <= 100: # Límite establecido para no saturar los hilos del procesador con el cálculo
      for i in range(numero + 1):
        print(factorial(i))
      break
    else:
      print("Error - Ingrese un numero entre 0 y 100")
  except ValueError:
    print("Error - Ingrese un número válido")

# Programa 2

def fibonacci(n):
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

while True:
  try:
    numero = int(input("Ingrese un número para calcular su posición en la sucesión de Fibonacci (0 - 20): "))
    if numero >= 0 and numero <= 20: # Límite establecido para no saturar los hilos del procesador con el cálculo
      for i in range(numero + 1):
        if i == numero:
          print(f"{fibonacci(i)} <- Este es el resultado en la posición que ingresaste")
        else:
          print(fibonacci(i))
      break
    else:
      print("Error - Ingrese un numero entre 0 y 20")
  except ValueError:
    print("Error - Ingrese un número válido")

# Programa 3

def potencia(n, m):
  if m == 0:
    return 1
  else:
    return n * potencia(n, m - 1)

print("Potencia de 2 ^ 3:")
print(f"Calculado recursivamente: {potencia(2, 3)}")
print(f"Calculado directamente: {2 ** 3}")

# Programa 4

def decimal_a_binario(n):
  if n == 0 or n == 1:
    return str(n)
  else:
    return decimal_a_binario(n // 2) + str(n % 2)

print(decimal_a_binario(7)) # 111
print(decimal_a_binario(17)) # 10001

# Programa 5

def es_palindromo(palabra):
  palabra = palabra.replace(" ", "").lower()
  if len(palabra) <= 1:
    return True
  elif palabra[0] != palabra[-1]:
    return False
  else:
    return es_palindromo(palabra[1:-1])

print(es_palindromo("Reconocer")) # True
print(es_palindromo("Casa")) # False

# Programa 6

def suma_digitos(n):
  if n < 10:
    return n
  else:
    return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(1234)) # 10
print(suma_digitos(9)) # 9

# Programa 7

def contar_bloques(n):
  if n == 0 or n == 1:
    return n
  else:
    return n + contar_bloques(n - 1)

print(contar_bloques(1)) # 1
print(contar_bloques(2)) # 3
print(contar_bloques(4)) # 10

# Programa 8

def contar_digito(numero, digito):
  if numero == 0:
    return 0
  else:
    if (numero % 10) == digito:
      conteo = 1
    else:
      conteo = 0
    return conteo + contar_digito(numero // 10, digito)

print(contar_digito(12233421, 2)) # 3
print(contar_digito(5555, 5)) # 4