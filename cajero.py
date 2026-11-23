# Proyecto final: Cajero automatico
# Programa realizado en Python

USUARIO = "usuario"
CONTRASENA = "1234"
SALDO_INICIAL = 100000
INTENTOS_MAXIMOS = 3


def iniciar_sesion():
    """Permite entrar al cajero con un maximo de tres intentos."""
    intentos = 0

    while intentos < INTENTOS_MAXIMOS:
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contrasena: ")

        if usuario == USUARIO and contrasena == CONTRASENA:
            print("\nBienvenido al cajero automatico.")
            return True
        else:
            intentos = intentos + 1
            faltan = INTENTOS_MAXIMOS - intentos
            print("Usuario o contrasena incorrectos.")
            print("Intentos restantes:", faltan)

    print("\nSe acabaron los intentos. El programa se cerrara.")
    return False


def consultar_saldo(saldo):
    print("\nSu saldo actual es: $", saldo)


def depositar_dinero(saldo):
    try:
        cantidad = float(input("Cuanto dinero desea depositar?: $"))

        if cantidad > 0:
            saldo = saldo + cantidad
            print("Deposito realizado correctamente.")
        else:
            print("Debe ingresar una cantidad mayor que cero.")

    except ValueError:
        print("Debe escribir un numero valido.")

    return saldo


def retirar_dinero(saldo):
    try:
        cantidad = float(input("Cuanto dinero desea retirar?: $"))

        if cantidad <= 0:
            print("El retiro debe ser mayor que cero.")
        elif cantidad > saldo:
            print("No tiene saldo suficiente para realizar el retiro.")
        else:
            saldo = saldo - cantidad
            print("Retiro realizado correctamente.")

    except ValueError:
        print("Debe escribir un numero valido.")

    return saldo


def mostrar_menu():
    print("\n------ CAJERO AUTOMATICO ------")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")


def ejecutar_cajero():
    saldo = SALDO_INICIAL

    if iniciar_sesion():
        opcion = ""

        while opcion != "4":
            mostrar_menu()
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                consultar_saldo(saldo)
            elif opcion == "2":
                saldo = depositar_dinero(saldo)
            elif opcion == "3":
                saldo = retirar_dinero(saldo)
            elif opcion == "4":
                print("Gracias por utilizar el cajero. Hasta pronto.")
            else:
                print("Opcion no valida. Intente otra vez.")


# Esta linea inicia el programa.
ejecutar_cajero()
