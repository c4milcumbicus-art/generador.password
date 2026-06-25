import random
import string

# Lista para guardar historial
historial = []

# Tupla con longitudes recomendadas
longitudes_recomendadas = (8, 12, 16, 20)

# Diccionario con grupos de caracteres
caracteres = {
    "mayusculas": string.ascii_uppercase,
    "minusculas": string.ascii_lowercase,
    "numeros": string.digits,
    "simbolos": "!@#$%&*?"
}


def generar_password(longitud, mayusculas, numeros, simbolos):

    password = []

    # Siempre incluir minúsculas
    conjunto = caracteres["minusculas"]

    if mayusculas:
        conjunto += caracteres["mayusculas"]
        password.append(random.choice(caracteres["mayusculas"]))

    if numeros:
        conjunto += caracteres["numeros"]
        password.append(random.choice(caracteres["numeros"]))

    if simbolos:
        conjunto += caracteres["simbolos"]
        password.append(random.choice(caracteres["simbolos"]))

    # Asegurar al menos una minúscula
    password.append(random.choice(caracteres["minusculas"]))

    # Completar el resto de caracteres
    while len(password) < longitud:
        password.append(random.choice(conjunto))

    # Mezclar para que no siga un patrón
    random.shuffle(password)

    return "".join(password)


def mostrar_historial():

    if len(historial) == 0:
        print("\nNo hay contraseñas generadas.")
        return

    print("\n===== HISTORIAL =====")

    for i, clave in enumerate(historial, start=1):
        print(f"{i}. {clave}")


def menu():

    while True:

        print("\n==============================")
        print(" GENERADOR DE CONTRASEÑAS ")
        print("==============================")
        print("Longitudes recomendadas:", longitudes_recomendadas)
        print("1. Generar contraseña")
        print("2. Ver historial")
        print("3. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            while True:

                try:
                    longitud = int(
                        input("Ingrese la longitud (mínimo 8): ")
                    )

                    if longitud >= 8:
                        break

                    print("La contraseña debe tener mínimo 8 caracteres.")

                except ValueError:
                    print("Ingrese un número válido.")

            mayusculas = input(
                "¿Incluir mayúsculas? (s/n): "
            ).lower() == "s"

            numeros = input(
                "¿Incluir números? (s/n): "
            ).lower() == "s"

            simbolos = input(
                "¿Incluir símbolos? (s/n): "
            ).lower() == "s"

            password = generar_password(
                longitud,
                mayusculas,
                numeros,
                simbolos
            )

            historial.append(password)

            print("\nContraseña generada:")
            print(password)

        elif opcion == "2":
            mostrar_historial()

        elif opcion == "3":
            print("\nGracias por usar el programa.")
            break

        else:
            print("\nOpción no válida.")


menu()
