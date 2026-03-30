# Programa 1

productos_suma_no_descuento = 0
productos_suma_con_descuento = 0
productos_ahorro = 0
productos_promedio_precio = 0

while True:
  nombre_cliente = input("Ingrese el nombre del cliente: ")
  if not nombre_cliente.strip():
    print("El nombre del cliente no puede estar vacío. Intente nuevamente.")
  else:
    if nombre_cliente.isalpha():
      break
    else:
      print("El nombre del cliente debe contener solo letras. Intente nuevamente.")

while True:
  cantidad_productos = input("Ingrese la cantidad de productos que desea comprar: ")
  if cantidad_productos.isdigit():
    if int(cantidad_productos) <= 0:
      print("La cantidad de productos debe ser mayor a 0. Intente nuevamente.")
    else:
      break
  else:
    if not cantidad_productos.strip():
      print("La cantidad de productos no puede estar vacía. Intente nuevamente.")
    else:
      print("La cantidad de productos debe ser un número entero. Intente nuevamente.")

for i in range(int(cantidad_productos)):
  while True:
    producto_precio = input(f"Ingrese el precio del producto {i + 1}: ")
    if producto_precio.isdigit():
      if float(producto_precio) <= 0:
        print("El precio del producto debe ser mayor a 0. Intente nuevamente.")
      else:
        productos_suma_no_descuento += float(producto_precio)
        break
    else:
      if not producto_precio.strip():
        print("El precio del producto no puede estar vacío. Intente nuevamente.")
      else:
        print("El precio del producto debe ser un número entero. Intente nuevamente.")
  while True:
    producto_descuento = input(f"El producto {i + 1} tiene descuento? (S/N): ")
    if producto_descuento.upper() in ["S", "N"]:
      if producto_descuento.upper() == "S":
        descuento = float(producto_precio) * 0.10
        productos_suma_con_descuento += float(producto_precio) - descuento
        productos_ahorro += descuento
        break
      else:
        productos_suma_con_descuento += float(producto_precio)
        break
    else:
      print("Respuesta inválida. Por favor ingrese 'S' para sí o 'N' para no.")

productos_promedio_precio = productos_suma_con_descuento / int(cantidad_productos)

print(f"""
Total sin descuentos: ${productos_suma_no_descuento:.2f}
Total con descuentos: ${productos_suma_con_descuento:.2f}
Ahorro: ${productos_ahorro:.2f}
Promedio por producto: ${productos_promedio_precio:.2f}""")

# Programa 2

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos_ingreso = 0

while True:
  usuario_ingresado = input("Ingrese su nombre de usuario: ")
  clave_ingresada = input("Ingrese su contraseña: ")

  if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
    while True:
      print(f"""
¡Bienvenido {usuario_ingresado}!
1. Ver estado de inscripion
2. Cambiar clave
3. Mostrar mensaje motivacional
4. Salir
""")
      opcion = input("Seleccione una opción: ")
      match opcion:
        case "1":
          print("Estado de inscripción: Inscrito")
        case "2":
          while True:
            nueva_clave = input("Ingrese su nueva contraseña: ")
            if not nueva_clave.strip() or " " in nueva_clave:
              print("La nueva contraseña no puede estar vacía, contener espacios en blanco o solo espacios. Intente nuevamente.")
            else:
              if len(nueva_clave) < 6:
                print("La nueva contraseña debe tener al menos 6 caracteres. Intente nuevamente.")
              else:
                while True:
                  confirmacion_nueva_clave = input("Confirme su nueva contraseña: ")
                  if nueva_clave == confirmacion_nueva_clave:
                    clave_correcta = nueva_clave
                    print("Contraseña actualizada exitosamente.")
                    break
                  else:
                    print("Las contraseñas no coinciden. Intente nuevamente.")
                break
        case "3":
          print("Si se puede IMAGINAR, se puede PROGRAMAR. - Alan Kay")
        case "4":
          print("¡Hasta luego!")
          break
        case _:
          if not int(opcion.isdigit()):
            print("Opción inválida. Por favor ingrese un número.")
          else:
            print("Opción inválida. Por favor seleccione una opción válida (1, 2, 3, 4).")
    break
  else:
    print("Usuario o contraseña incorrectos. Intente nuevamente.")
    intentos_ingreso += 1
    if intentos_ingreso >= 3:
      print("Has excedido el número de intentos. Cuenta bloqueada.")
      break

# Programa 3

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

sistema_cerrado = False

while True:
  nombre_operador = input("Ingrese su nombre de operador: ")
  if not nombre_operador.strip():
    print("El nombre de operador no puede estar vacío. Intente nuevamente.")
  else:
    nombre_operador_correcto = True
    for i in nombre_operador:
      if not i.isalpha():
        print("El nombre de operador debe contener solo letras. Intente nuevamente.")
        nombre_operador_correcto = False
        break
    if nombre_operador_correcto:
      while True:
        print(f"""
¡Bienvenido {nombre_operador}!
1. Reservar turno
2. Cancelar turno (por nombre)
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema
""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1" or opcion == "2" or opcion == "3":
          while True:
            dia = input("Seleccione día (1 = Lunes, 2 = Martes): ")
            if dia.isdigit():
              if dia == "1" or dia == "2":
                break
              else:
                print("Día inválido. Debe ingresar 1 o 2.")
            else:
              if not dia.strip():
                print("El día no puede estar vacío. Intente nuevamente.")
              else:
                print("El día debe ser un número entero. Intente nuevamente.")
        if opcion == "1" or opcion == "2":
          while True:
            nombre_paciente = input("Ingrese el nombre del paciente: ")
            if not nombre_paciente.strip():
              print("El nombre del paciente no puede estar vacío. Intente nuevamente.")
            else:
              nombre_paciente_correcto = True
              for letra in nombre_paciente:
                if not letra.isalpha():
                  print("El nombre del paciente debe contener solo letras. Intente nuevamente.")
                  nombre_paciente_correcto = False
                  break
              if nombre_paciente_correcto:
                break
        if opcion == "1" or opcion == "2" or opcion == "3":
          if dia == "1":
            nombre_dia = "Lunes"
            cupos_dia = 4
            turno1 = lunes1
            turno2 = lunes2
            turno3 = lunes3
            turno4 = lunes4
          else:
            nombre_dia = "Martes"
            cupos_dia = 3
            turno1 = martes1
            turno2 = martes2
            turno3 = martes3
            turno4 = ""
        match opcion:
          case "1":
            if (turno1 != "" and turno1.lower() == nombre_paciente.lower()) or (turno2 != "" and turno2.lower() == nombre_paciente.lower()) or (turno3 != "" and turno3.lower() == nombre_paciente.lower()) or (cupos_dia == 4 and turno4 != "" and turno4.lower() == nombre_paciente.lower()):
              print(f"Ese paciente ya tiene turno en {nombre_dia}.")
            elif turno1 == "":
              turno1 = nombre_paciente
              print(f"Turno reservado en {nombre_dia} (Turno 1).")
            elif turno2 == "":
              turno2 = nombre_paciente
              print(f"Turno reservado en {nombre_dia} (Turno 2).")
            elif turno3 == "":
              turno3 = nombre_paciente
              print(f"Turno reservado en {nombre_dia} (Turno 3).")
            elif cupos_dia == 4 and turno4 == "":
              turno4 = nombre_paciente
              print(f"Turno reservado en {nombre_dia} (Turno 4).")
            else:
              print(f"No hay cupos disponibles en {nombre_dia}.")
            if dia == "1":
              lunes1 = turno1
              lunes2 = turno2
              lunes3 = turno3
              lunes4 = turno4
            else:
              martes1 = turno1
              martes2 = turno2
              martes3 = turno3
          case "2":
            if turno1 != "" and turno1.lower() == nombre_paciente.lower():
              turno1 = ""
              print(f"Turno cancelado en {nombre_dia} (Turno 1).")
            elif turno2 != "" and turno2.lower() == nombre_paciente.lower():
              turno2 = ""
              print(f"Turno cancelado en {nombre_dia} (Turno 2).")
            elif turno3 != "" and turno3.lower() == nombre_paciente.lower():
              turno3 = ""
              print(f"Turno cancelado en {nombre_dia} (Turno 3).")
            elif cupos_dia == 4 and turno4 != "" and turno4.lower() == nombre_paciente.lower():
              turno4 = ""
              print(f"Turno cancelado en {nombre_dia} (Turno 4).")
            else:
              print(f"Paciente no encontrado en la agenda de {nombre_dia}.")
            if dia == "1":
              lunes1 = turno1
              lunes2 = turno2
              lunes3 = turno3
              lunes4 = turno4
            else:
              martes1 = turno1
              martes2 = turno2
              martes3 = turno3
          case "3":
            print(f"\nAgenda de {nombre_dia}")
            print(f"Turno 1: {turno1 if turno1 != '' else '(libre)'}")
            print(f"Turno 2: {turno2 if turno2 != '' else '(libre)'}")
            print(f"Turno 3: {turno3 if turno3 != '' else '(libre)'}")
            if cupos_dia == 4:
              print(f"Turno 4: {turno4 if turno4 != '' else '(libre)'}")
          case "4":
            ocupados_lunes = 0
            ocupados_martes = 0
            if lunes1 != "":
              ocupados_lunes += 1
            if lunes2 != "":
              ocupados_lunes += 1
            if lunes3 != "":
              ocupados_lunes += 1
            if lunes4 != "":
              ocupados_lunes += 1
            if martes1 != "":
              ocupados_martes += 1
            if martes2 != "":
              ocupados_martes += 1
            if martes3 != "":
              ocupados_martes += 1
            disponibles_lunes = 4 - ocupados_lunes
            disponibles_martes = 3 - ocupados_martes
            print("\nResumen general")
            print(f"Lunes > Ocupados: {ocupados_lunes} | Disponibles: {disponibles_lunes}")
            print(f"Martes > Ocupados: {ocupados_martes} | Disponibles: {disponibles_martes}")
            if ocupados_lunes > ocupados_martes:
              print("Día con más turnos: Lunes")
            elif ocupados_martes > ocupados_lunes:
              print("Día con más turnos: Martes")
            else:
              print("Día con más turnos: Empate")
          case "5":
            print("Cerrando sistema...")
            sistema_cerrado = True
            break
          case _:
            print("Opción inválida. Por favor seleccione una opción válida.")
      if sistema_cerrado:
        break

# Programa 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

cantidad_forzadas = 0
bloqueo_alarma = False

while True:
  nombre_agente = input("Ingrese el nombre del agente: ")
  if not nombre_agente.strip():
    print("Nombre inválido. Por favor ingrese un nombre válido.")
  elif nombre_agente.isalpha():
    print(f"Bienvenido, agente {nombre_agente}.")
    break
  else:
    print("Nombre inválido. Por favor ingrese un nombre válido.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
  if alarma and tiempo <= 3:
    bloqueo_alarma = True
    break
  print(f"""
|| Estadisticas:
> Energía: {energia}
> Tiempo: {tiempo}
> Cerraduras abiertas: {cerraduras_abiertas}
> Alarma: {"Activada" if alarma else "Desactivada"}
> Código parcial: {codigo_parcial if codigo_parcial != '' else '(vacío)'}
|| Opciones:
1. Forzar cerradura (costo: -20 energía, -2 tiempo)
2. Hackear panel (costo: -10 energía, -3 tiempo)
3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)
""")
  while True:
    opcion = input("Seleccione una opción (1, 2 o 3): ")
    if opcion.isdigit():
      if opcion == "1" or opcion == "2" or opcion == "3":
        break
      else:
        print("Opción inválida. Por favor seleccione una opción válida.")
    else:
      print("Opción inválida. Por favor ingrese un número válido.")
  match opcion:
    case "1":
      cantidad_forzadas += 1
      energia -= 20
      tiempo -= 2
      if cantidad_forzadas >= 3:
        alarma = True
        print("La cerradura se trabó por forzar 3 veces seguidas. Alarma activada.")
        print("No se abrió cerradura en este turno.")
      else:
        if energia < 40:
          while True:
            numero_reducir_alarma = input("Energía baja: ingrese un número del 1 al 3: ")
            if not numero_reducir_alarma.isdigit():
              print("Número inválido. Por favor ingrese un número.")
            elif int(numero_reducir_alarma) < 1 or int(numero_reducir_alarma) > 3:
              print("Número inválido. Por favor ingrese un número entre 1 y 3.")
            else:
              if numero_reducir_alarma == "3":
                print("Mala suerte. Alarma activada.")
                alarma = True
              else:
                print("Riesgo superado.")
              break
        if not alarma:
          cerraduras_abiertas += 1
          print("Has forzado la cerradura con éxito.")
        else:
          print("No se abrió cerradura porque la alarma está activada.")
    case "2":
      cantidad_forzadas = 0
      energia -= 10
      tiempo -= 3
      for paso in range(1, 5):
        codigo_parcial += "A"
        print(f"Hackeo en progreso {paso}/4... Código parcial: {codigo_parcial}")
      if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
        cerraduras_abiertas += 1
        print("Hackeo exitoso: se abrió 1 cerradura automáticamente.")
    case "3":
      cantidad_forzadas = 0
      energia += 15
      if energia > 100:
        energia = 100
      tiempo -= 1
      if alarma:
        energia -= 10
        print("Descansaste con alarma activa: perdiste 10 de energía extra.")
      print("Descanso completado.")

if cerraduras_abiertas >= 3:
  print("¡VICTORIA! Abriste las 3 cerraduras de la bóveda.")
elif bloqueo_alarma:
  print("DERROTA: bloqueo por alarma (alarma activa con tiempo crítico).")
else:
  print("DERROTA: te quedaste sin energía o sin tiempo.")

# Programa 5

vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
dano_ataque_pesado = 15
dano_enemigo = 12
turno_gladiador = True

while True:
  nombre_gladiador = input("Nombre del Gladiador: ")
  if not nombre_gladiador.strip():
    print("Error: Solo se permiten letras")
  else:
    nombre_valido = True
    for letra in nombre_gladiador:
      if not letra.isalpha():
        nombre_valido = False
    if nombre_valido == False:
      print("Error: Solo se permiten letras")
    else:
      break

print("=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0:
  if turno_gladiador == True:
    print("")
    print(f"{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    while True:
      opcion = input("Opción: ")
      if opcion.isdigit():
        if opcion == "1" or opcion == "2" or opcion == "3":
          break
        else:
          print("Error: Ingrese un número válido.")
      else:
        print("Error: Ingrese un número válido.")
    if opcion == "1":
      dano_base = float(dano_ataque_pesado)
      if vida_enemigo < 20:
        dano_final = dano_base * 1.5
      else:
        dano_final = dano_base
      vida_enemigo = vida_enemigo - dano_final
      print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")
    elif opcion == "2":
      print(">> ¡Inicias una ráfaga de golpes!")
      for i in range(3):
        vida_enemigo = vida_enemigo - 5
        print("> Golpe conectado por 5 de daño")
        if vida_enemigo <= 0:
          vida_enemigo = 0
          break
    elif opcion == "3":
      if pociones_vida > 0:
        vida_gladiador = vida_gladiador + 30
        if vida_gladiador > 100:
          vida_gladiador = 100
        pociones_vida = pociones_vida - 1
        print(">> Te has curado.")
      else:
        print("¡No quedan pociones!")
    turno_gladiador = False
  else:
    if vida_enemigo > 0:
      vida_gladiador = vida_gladiador - dano_enemigo
      print(f">> ¡El enemigo te atacó por {dano_enemigo} puntos de daño!")
    turno_gladiador = True

print("")
print("=== FIN DEL JUEGO ===")
if vida_gladiador > 0:
  print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
  print("DERROTA. Has caído en combate.")