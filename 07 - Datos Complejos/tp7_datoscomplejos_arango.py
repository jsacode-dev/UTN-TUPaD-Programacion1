# Juan Santiago Arango - 54193

def validar_str(mensaje):
  while True:
    texto = input(mensaje).strip()
    if texto != "":
      return texto
    else:
      print("Entrada inválida. Por favor, ingrese un texto válido.")

def validar_numero_int(mensaje):
  while True:
    numero = input(mensaje).strip()
    if numero.isdigit() and numero != "":
      return int(numero)
    else:
      print("Entrada inválida. Por favor, ingrese un número válido.")

# Programa 1

precios_frutas = { "Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450 }
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

# Programa 2

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# Programa 3

frutas = list(precios_frutas.keys())
print(frutas)

# Programa 4

def cargar_contactos(cantidad):
  contactos = {}
  for i in range(cantidad):
    nombre = validar_str(f"Ingrese el nombre del contacto {i + 1}: ").capitalize()
    telefono = validar_numero_int(f"Ingrese el número de teléfono del contacto {i + 1}: ")
    contactos[nombre] = telefono
  return contactos

cantidad_contactos = validar_numero_int("¿Cuántos contactos desea ingresar? ")
agenda_contactos = cargar_contactos(cantidad_contactos)

def buscar_contacto(agenda, nombre):
  return agenda.get(nombre, "Contacto no encontrado.")

while True:
  nombre_busqueda = validar_str("Ingrese el nombre del contacto que desea buscar (o 1 para terminar): ")
  if nombre_busqueda == "1":
    break
  resultado = buscar_contacto(agenda_contactos, nombre_busqueda.capitalize())
  print(resultado)

# Programa 5

def palabras_unicas(frase):
  palabras = frase.split()
  palabras_unicas = set(palabras)
  return palabras_unicas

def recuento(frase):
  palabras = frase.split()
  recuento_palabras = {}
  for palabra in palabras:
    if palabra in recuento_palabras:
      recuento_palabras[palabra] += 1
    else:
      recuento_palabras[palabra] = 1
  return recuento_palabras

frase = validar_str("Ingrese una frase: ").strip().lower()
print("Palabras únicas:", palabras_unicas(frase))
print("Recuento de palabras:", recuento(frase))

# Programa 6

def ingresar_alumnos():
  alumnos = {}
  for i in range(3):
    nombre = validar_str(f"Ingrese el nombre del alumno {i + 1}: ").capitalize()
    notas = []
    for j in range(3):
      nota = validar_numero_int(f"Ingrese la nota {j + 1} del alumno {nombre}: ")
      notas.append(nota)
    alumnos[nombre] = tuple(notas)
  return alumnos

alumnos_notas = ingresar_alumnos()

print(alumnos_notas)

for i in range(3):
  print(f"Alumno: {list(alumnos_notas.keys())[i]}, Promedio: {sum(alumnos_notas[list(alumnos_notas.keys())[i]]) / 3:.2f}")

# Programa 7

def asistencias_unicas(asistencias):
  numero_asistencias = {}
  set_asistencias = set(asistencias)
  for persona in list(set_asistencias):
    numero_asistencias[persona] = asistencias.count(persona)
  return numero_asistencias

asistencias = ["Ana", "Luis", "Ana", "María", "Luis", "Pedro", "Ana"]

print(asistencias)
print(set(asistencias))
print(asistencias_unicas(asistencias))

# Programa 8

productos_stock = {
  "Laptop": 10,
  "Smartphone": 25,
  "Tablet": 15,
  "Auriculares": 30,
}

def consultar_stock(producto):
  return productos_stock.get(producto, "Producto no encontrado.")

def agregar_stock(producto, cantidad):
  if producto in productos_stock:
    productos_stock[producto] += cantidad
    print(f"Stock actualizado para {producto}: {productos_stock[producto]}")
  else:
    print("Producto no encontrado. Use la opción para agregar un nuevo producto.")

def agregar_nuevo_producto(producto, cantidad):
  if producto in productos_stock:
    print("El producto ya existe. Use la opción para agregar stock.")
  else:
    productos_stock[producto] = cantidad
    print(f"Producto {producto} agregado con stock inicial de {cantidad}.")

while True:
  opcion = validar_numero_int("Ingrese una opción (1 para consultar stock, 2 para agregar stock, 3 para agregar nuevo producto, 0 para salir): ")
  match opcion:
    case 1:
      producto_consulta = validar_str("Ingrese el nombre del producto a consultar: ")
      print(f"Stock de {producto_consulta}: {consultar_stock(producto_consulta)}")
    case 2:
      producto_agregar = validar_str("Ingrese el nombre del producto al que desea agregar stock: ")
      cantidad_agregar = validar_numero_int("Ingrese la cantidad a agregar: ")
      agregar_stock(producto_agregar, cantidad_agregar)
    case 3:
      nuevo_producto = validar_str("Ingrese el nombre del nuevo producto: ")
      stock_inicial = validar_numero_int("Ingrese el stock inicial para el nuevo producto: ")
      agregar_nuevo_producto(nuevo_producto, stock_inicial)
    case 0:
      print("Saliendo del programa.")
      break
    case _:
      print("Opción no válida. Por favor, ingrese una opción correcta.")

# Programa 9

agenda = {
  ("lunes", "10:00"): "Reunión",
  ("martes", "15:00"): "Clase de inglés",
}

def consultar_actividad(agenda, dia, hora):
  return agenda.get((dia, hora), "No hay actividad programada.")

dia_consulta = validar_str("Ingrese el día de la semana para consultar: ").lower()
hora_consulta = validar_str("Ingrese la hora para consultar (formato HH:MM): ")
actividad = consultar_actividad(agenda, dia_consulta, hora_consulta)
print(f"Actividad programada para {dia_consulta} a las {hora_consulta}: {actividad}")

# Programa 10

original = {
  "Argentina": "Buenos Aires",
  "Chile": "Santiago",
}
invertido = {}

for pais, capital in original.items():
  invertido[capital] = pais

print("Diccionario original:", original)
print("Diccionario invertido:", invertido)