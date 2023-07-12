def login():
    while True:
        user = input("Ingrese el usuario: ")
        password = input("Ingrese la contraseña: ")

        if user == "hmayorga" and password == "1234":
            return "alumno"
        elif user == "usuario_prueba" and password == "5678":  # Usuario a modo de prueba (puedes cambiarlo)
            return "alumno"
        elif user == "admin" and password == "admin123":  # Usuario administrativo (puedes cambiarlo)
            return "admin"
        else:
            print("Credenciales inválidas. Intente nuevamente.\n")


def mostrar_menu():
    print("===== MENÚ DE SERVICIOS =====")
    print("1. Impresión B/N ($150 por hoja)")
    print("2. Impresión Color ($300 por hoja)")
    print("3. Fotocopias ($80 por hoja)")
    print("4. Anillados ($5.000 por informe)")
    print("5. Anular pedido")
    print("6. Salir")
    print()


def calcular_descuento(total, tipo_usuario):
    if tipo_usuario == "alumno":
        modalidad = input("Ingrese la modalidad del alumno (diurna o vespertina): ")
        if modalidad.lower() == "diurna":
            total *= 0.9  # Descuento del 10% para alumnos diurnos
        elif modalidad.lower() == "vespertina":
            total *= 0.8  # Descuento del 20% para alumnos vespertinos
    return total


def realizar_pedido(tipo_usuario):
    total_pedido = 0

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            cantidad_bn = int(input("Ingrese la cantidad de hojas para impresión B/N: "))
            total_pedido += cantidad_bn * 150
        elif opcion == "2":
            cantidad_color = int(input("Ingrese la cantidad de hojas para impresión color: "))
            total_pedido += cantidad_color * 300
        elif opcion == "3":
            cantidad_fotocopias = int(input("Ingrese la cantidad de hojas para fotocopias: "))
            total_pedido += cantidad_fotocopias * 80
        elif opcion == "4":
            cantidad_anillados = int(input("Ingrese la cantidad de informes para anillar: "))
            total_pedido += cantidad_anillados * 5000
        elif opcion == "5":
            print("Pedido anulado.\n")
            return None
        elif opcion == "6":
            return total_pedido
        else:
            print("Opción inválida. Intente nuevamente.\n")

        print("Pedido actual:", total_pedido)


def dividir_pago(total_pedido):
    while True:
        num_personas = int(input("Ingrese el número de personas para dividir el pago: "))

        try:
            pago_individual = total_pedido / num_personas
            print("El pago por persona es:", pago_individual)
            break
        except ZeroDivisionError:
            print("Error: el número de personas debe ser mayor que cero. Intente nuevamente.\n")
        except Exception as e:
            print("Error:", str(e))
            break


tipo_usuario = login()
if tipo_usuario == "admin":
    print("Bienvenido, administrativo.")
else:
    print("Bienvenido, alumno.")
    total_pedido = realizar_pedido(tipo_usuario)

    if total_pedido is not None:
        total_pedido = calcular_descuento(total_pedido, tipo_usuario)
        print("\nTotal a pagar:", total_pedido)
        print("Gracias por su compra.\n")
        dividir_pago(total_pedido)
