# Juan Santiago Arango - TP5 Listas

# Ejercicio 1

notas_estudiantes = [7, 8, 9, 10, 6, 5, 10, 8, 2, 7]

for i in range(len(notas_estudiantes)):
    print(f"Nota del estudiante {i + 1}: {notas_estudiantes[i]}")
print("")
print(f"Promedio de notas: {sum(notas_estudiantes) / len(notas_estudiantes):.2f}")
print(f"Nota mas alta: {max(notas_estudiantes)} / Nota mas baja: {min(notas_estudiantes)}")

# Ejercicio 2

productos = []

for i in range(5):
  producto = input(f"Ingrese el producto {i + 1}: ")
  productos.append(producto)

productos = sorted(productos)
print("Los productos son: ", end="")
for i in productos:
  if i == productos[-1]:
    print(i)
  else:
    print(i, end=", ")

print("= = = = = = = = = =")
print("Que desea hacer?")
print("> 1. Eliminar elemento")
print("> 2. Editar elemento")
accion = int(input())

match accion:
  case 1:
    print("= = = = = = = = = =")
    print("Que elemento desea eliminar?")
    for i in range(len(productos)):
      print(f"> {i + 1}. {productos[i]}")
    eliminarelemento = int(input())
    for i in range(len(productos)):
      if 0 <= eliminarelemento <= len(productos):
        if (i + 1) == eliminarelemento:
          productos.remove(productos[i])
          print(f"-> El producto {i + 1} fue eliminado")
          productos = sorted(productos)
          print("Ahora los productos son: ", end="")
          for i in productos:
            if i == productos[-1]:
              print(i)
            else:
              print(i, end=", ")
      else:
        print("Es opcion no estaba en la lista. Reintentelo")
        break
  case 2:
    print("= = = = = = = = = =")
    print("Que elemento desea editar?")
    for i in range(len(productos)):
      print(f"> {i + 1}. {productos[i]}")
    editarelemento = int(input())
    for i in range(len(productos)):
      if 0 <= editarelemento <= len(productos):
        if (i + 1) == editarelemento:
          nuevovalorelemento = input(f"Ingresa el nuevo valor para el elemento {i + 1}: ")
          tempvalor = productos[i]
          productos[i] = nuevovalorelemento
          print(f"-> Se cambio el valor del producto {i + 1} de '{tempvalor}' a '{nuevovalorelemento}'")
          productos = sorted(productos)
          print("Ahora los productos son: ", end="")
          for i in productos:
            if i == productos[-1]:
              print(i)
            else:
              print(i, end=", ")
      else:
        print("Es opcion no estaba en la lista. Reintentelo")
        break
  case _:
    print("Es opcion no estaba en la lista. Reintentelo")

# Ejercicio 3

import random

numeros = [random.randint(1, 100) for _ in range(15)]
numeros_pares = []
numeros_impares = []

for numero in numeros:
  if numero % 2 == 0:
    numeros_pares.append(numero)
  else:
    numeros_impares.append(numero)

print(f"Numeros pares: {len(numeros_pares)} / Numeros impares: {len(numeros_impares)}")

# Ejercicio 4

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_unicos = []

for i in datos:
  if i not in datos_unicos:
    datos_unicos.append(i)

print("Lista sin elementos repetidos: ", end="")
for i in range(len(datos_unicos)):
  if i < len(datos_unicos) - 1:
    print(f"{datos_unicos[i]}, ", end="")
  else:
    print(f"{datos_unicos[i]}")

# Ejercicio 5

estudiantes_presentes = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Lucía"]

while True:
  print("Estudiantes presentes:")
  for i in range(len(estudiantes_presentes)):
    print(f"> Estudiante {i + 1}: {estudiantes_presentes[i]}")

  estudiante_seleccionado = input("¿Desea agregar un nuevo estudiante o eliminar uno existente? (a, e, 0 para salir): ").lower()
  if estudiante_seleccionado == "0":
    break
  elif estudiante_seleccionado == "a":
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes_presentes.append(nuevo_estudiante)
    print(f"Estudiante {nuevo_estudiante} agregado.\n")
  elif estudiante_seleccionado == "e":
    while True:
      indice_eliminar = input("Ingrese el número del estudiante que desea eliminar: ")
      if indice_eliminar.isdigit():
        indice_eliminar = int(indice_eliminar)
        if 1 <= indice_eliminar <= len(estudiantes_presentes):
          estudiante_eliminado = estudiantes_presentes.pop(indice_eliminar - 1)
          print(f"Estudiante {estudiante_eliminado} eliminado.\n")
          break
        else:
          print("Número de estudiante fuera de rango. Intente nuevamente.\n")
      else:
        print("Entrada no válida. Por favor ingrese un número.\n")
  else:
    print("Opción no válida. Intente nuevamente.\n")

# Ejercicio 6

numeros = [1, 2, 3, 4, 5, 6, 7]

print(numeros)
for i in range(len(numeros)):
  ultimoelemento = numeros.pop()
  numeros.insert(0, ultimoelemento)
  print(numeros)

# Ejercicio 7

matriztemperatura = [
  [28, 19],
  [32, 19],
  [31, 17],
  [22, 14],
  [27, 16],
  [29, 18],
  [33, 21]
]
sumamin = 0
sumamax = 0
amplitudestermicas = []
diamayoramptermica = []

for i in range(len(matriztemperatura)):
  sumamin += matriztemperatura[i][1]
  sumamax += matriztemperatura[i][0]
  amplitudestermicas.append(matriztemperatura[i][0] - matriztemperatura[i][1])
  diamayoramptermica = [max(amplitudestermicas), (amplitudestermicas.index(max(amplitudestermicas)) + 1), [matriztemperatura[amplitudestermicas.index(max(amplitudestermicas))][0], matriztemperatura[amplitudestermicas.index(max(amplitudestermicas))][1]]]
promediomin = sumamin / len(matriztemperatura)
promediomax = sumamax / len(matriztemperatura)

print(f"El promedio de las temperaturas minimas fue {round(promediomin, 2)} y el de las temperaturas maximas fue {round(promediomax, 2)}")
print(f"En el dia {diamayoramptermica[1]} se registro la mayor amplitud termica, siendo de {diamayoramptermica[0]} ({diamayoramptermica[2][0]} - {diamayoramptermica[2][1]})")

# Ejercicio 8

matriznotasmaterias = [
  [8, 8, 6],
  [10, 4, 5],
  [6, 6, 9],
  [9, 8, 10],
  [5, 9, 8]
]
sumasestudiantes = []
sumasmaterias = []

for i in matriznotasmaterias[0]:
  sumasmaterias.append(0)
for i in matriznotasmaterias:
  sumasestudiantes.append(sum(i))
  for j in range(len(i)):
    sumasmaterias[j] += i[j]

for i in range(len(sumasestudiantes)):
  print(f"El promedio del estudiante {i + 1} es {sumasestudiantes[i] / len(sumasestudiantes)}")
print("= = = = = = = = = =")
for i in range(len(sumasmaterias)):
  print(f"El promedio de la materia {i + 1} es {round((sumasmaterias[i] / len(sumasmaterias)), 2)}")

# Ejercicio 9

tateti = [
  [" - ", " - ", " - "],
  [" - ", " - ", " - "],
  [" - ", " - ", " - "]
]
jx_posiciones = []
jo_posiciones = []

for i in tateti:
  for j in i:
    print(j, end="")
  print("")
print("= = = = = = = = = = =")

while True:
  while True:
    while True:
      jx_fila = int(input(f"Jugador X > Ingrese la fila (1 - {len(tateti)}): "))
      if (1 <= jx_fila <= len(tateti)):
        break
      else:
        print("Es opcion no estaba en la lista. Reintentelo")
        print("- - - - - - - - - - -")
        pass
    while True:
      jx_columna = int(input(f"Jugador X > Ingrese la columna (1 - {len(tateti)}): "))
      if 1 <= jx_columna <= len(tateti):
        break
      else:
        print("Es opcion no estaba en la lista. Reintentelo")
        print("- - - - - - - - - - -")
        pass
    if [jx_fila, jx_columna] in jx_posiciones or [jx_fila, jx_columna] in jo_posiciones:
      print("Esa casilla ya esta ocupada. Reintentelo")
      print("- - - - - - - - - - -")
      continue
    else:
      break
  print("= = = = = = = = = = =")
  for i in range(len(tateti)):
    for j in range(len(tateti)):
      if ((i + 1) == jx_fila) and ((j + 1) == jx_columna):
        tateti[i][j] = " X "
  for i in tateti:
    for j in i:
      print(j, end="")
    print("")
  jx_posiciones.append([jx_fila, jx_columna])
  print("= = = = = = = = = = =")
  
  if len(jx_posiciones) + len(jo_posiciones) == 9:
    print("El juego ha terminado: todas las casillas están ocupadas.")
    break
  
  while True:
    while True:
      jo_fila = int(input(f"Jugador O > Ingrese la fila (1 - {len(tateti)}): "))
      if (1 <= jo_fila <= len(tateti)):
        break
      else:
        print("Es opcion no estaba en la lista. Reintentelo")
        print("- - - - - - - - - - -")
        pass
    while True:
      jo_columna = int(input(f"Jugador X > Ingrese la columna (1 - {len(tateti)}): "))
      if 1 <= jo_columna <= len(tateti):
        break
      else:
        print("Es opcion no estaba en la lista. Reintentelo")
        print("- - - - - - - - - - -")
        pass
    if [jo_fila, jo_columna] in jx_posiciones or [jo_fila, jo_columna] in jo_posiciones:
      print("Esa casilla ya esta ocupada. Reintentelo")
      print("- - - - - - - - - - -")
      continue
    else:
      break
  print("= = = = = = = = = = =")
  for i in range(len(tateti)):
    for j in range(len(tateti)):
      if ((i + 1) == jo_fila) and ((j + 1) == jo_columna):
        tateti[i][j] = " O "
  for i in tateti:
    for j in i:
      print(j, end="")
    print("")
  jo_posiciones.append([jo_fila, jo_columna])
  print("= = = = = = = = = = =")
  
  if len(jx_posiciones) + len(jo_posiciones) == 9:
    print("El juego ha terminado: todas las casillas están ocupadas.")
    break

# Ejercicio 10

ventasproductos = [
  [12, 15, 14, 10, 18, 20, 22],
  [8, 6, 9, 11, 10, 13, 12],
  [20, 18, 22, 25, 19, 25, 21],
  [5, 7, 6, 4, 8, 9, 10]
]
totalvendidoproducto = []
ventastotalespordia = []

for i in ventasproductos:
  totalvendidoproducto.append(sum(i))

for i in ventasproductos[0]:
  ventastotalespordia.append(0)
for i in range(len(ventasproductos)):
  for j in range(len(ventasproductos[i])):
    ventastotalespordia[j] += ventasproductos[i][j]

print("Las ventas totales de cada producto son:")
for i in range(len(totalvendidoproducto)):
  print(f"> {i + 1}. {totalvendidoproducto[i]}")
print("= = = = = = = = = =")
print(f"El dia con mayores ventas totales es el dia {(ventastotalespordia.index(max(ventastotalespordia))) + 1} ({max(ventastotalespordia)} ventas)")
print("= = = = = = = = = =")
print(f"El producto mas vendido de la semana es el producto {(totalvendidoproducto.index(max(totalvendidoproducto))) + 1} ({max(totalvendidoproducto)} ventas)")

# Ejercicio 11

estudiantes = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Lucía", "Diego", "Valentina"]

estudiante_nombre = input("Ingrese el nombre del estudiante al que busca: ").lower()
if estudiante_nombre in [estudiante.lower() for estudiante in estudiantes]:
  print(f"El estudiante {estudiante_nombre.capitalize()} se encuentra en la lista. Esta en la posicion {estudiantes.index(estudiante_nombre.capitalize()) + 1} (indice {estudiantes.index(estudiante_nombre.capitalize())})")
else:
  print(f"El estudiante {estudiante_nombre.capitalize()} no se encuentra en la lista.")

# Ejercicio 12

numeros = []

print("Ingrese 8 numeros enteros: ")
for i in range(8):
  while True:
    numero = input(f"Num. {i + 1}: ").strip()
    if numero.isdigit():
      numeros.append(int(numero))
      break
    else:
      print("Por favor, ingrese un numero entero valido.")

print("Los numeros ingresados son: ", end="")
for i in numeros:
  if i == numeros[-1]:
    print(i)
  else:
    print(i, end=", ")

numeros_ordenados_me_ma = sorted(numeros)
print("Los numeros ordenados de menor a mayor son: ", end="")
for i in numeros_ordenados_me_ma:
  if i == numeros_ordenados_me_ma[-1]:
    print(i)
  else:
    print(i, end=", ")

numeros_ordenados_ma_me = sorted(numeros, reverse=True) # O puede usarse numeros_ordenados_me_ma[::-1]
print("Los numeros ordenados de mayor a menor son: ", end="")
for i in numeros_ordenados_ma_me:
  if i == numeros_ordenados_ma_me[-1]:
    print(i)
  else:
    print(i, end=", ")

# Ejercicio 13

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print(f"El puntaje más alto es {max(puntajes)} y el puntaje más bajo es {min(puntajes)}\n")

puntajes_ranking = sorted(puntajes, reverse=True)
print("Ranking:")
for i in range(len(puntajes_ranking)):
  print(f"{i + 1}. {puntajes_ranking[i]}")

print(f"El puntaje 990 se encuentra en la posición {puntajes_ranking.index(990) + 1} (indice {puntajes_ranking.index(990)})")