# Juan Santiago Arango - 54193

# Programa 2

with open("productos.txt", "r") as archivo:
  for linea in archivo:
    nombre, precio, cantidad = linea.strip().split(",")
    print(f"Producto: {nombre.capitalize()} | Precio: ${precio} | Cantidad: {cantidad}")

# Programa 3

def preguntar_producto():
  while True:
    try:
      nombre = input("Ingrese el nombre del producto: ").strip().lower()
      precio = float(input("Ingrese el precio del producto: ").strip())
      cantidad = int(input("Ingrese la cantidad del producto: ").strip())
      return nombre, precio, cantidad
    except ValueError:
      print("Entrada inválida. Por favor, ingrese un valor numérico para el precio y la cantidad.")
    except Exception as e:
      print(f"Ocurrió un error: {e}. Por favor, intente nuevamente.")

def ingresar_producto(nombre, precio, cantidad):
  with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")
  print("Producto ingresado correctamente.")

nombre, precio, cantidad = preguntar_producto()
ingresar_producto(nombre, precio, cantidad)

# Programa 4

productos = []
with open("productos.txt", "r") as archivo:
  for linea in archivo:
    nombre, precio, cantidad = linea.strip().split(",")
    producto = {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
    productos.append(producto)

print(productos)

# Programa 5

def buscar_por_nombre(nombre):
  with open("productos.txt", "r") as archivo:
    for linea in archivo:
      nombre_producto, precio, cantidad = linea.strip().split(",")
      if nombre_producto.lower() == nombre.lower():
        return {"nombre": nombre_producto, "precio": float(precio), "cantidad": int(cantidad)}
  return None

nombre_busqueda = input("Ingrese el nombre del producto a buscar: ").strip()
producto_encontrado = buscar_por_nombre(nombre_busqueda)
if producto_encontrado:
  print(f"Producto encontrado: {producto_encontrado["nombre"].capitalize()} | Precio: ${producto_encontrado["precio"]} | Cantidad: {producto_encontrado["cantidad"]}")
else:
  print("Producto no encontrado.")

# Programa 6

with open("productos.txt", "w") as archivo:
  for producto in productos:
    archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")