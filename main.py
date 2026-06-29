"""
Proyecto Integrador - SecureGen
Generador inteligente de contrasenas seguras

Asignatura : Programacion / Estructuras de Datos y Funciones (Unidad 4)
Universidad: UIDE
Descripcion: Aplicacion de consola que genera contrasenas seguras a partir
             de las preferencias del usuario y conserva un historial de las
             contrasenas generadas durante la sesion.

Estructuras de datos integradas (Unidad 4 - Tema 1):
    - TUPLA      -> longitudes_recomendadas  (valores fijos e inmutables)
    - DICCIONARIO-> caracteres               (conjuntos de caracteres por clave)
    - LISTA      -> historial                (coleccion mutable de contrasenas)

Funciones integradas (Unidad 4 - Tema 2):
    - generar_password()  -> funcion con parametros y valor de retorno (str)
    - mostrar_historial()  -> funcion sin parametros, recorre una lista
    - menu()               -> funcion principal, controla el flujo del programa

Estructuras logicas aplicadas:
    - Condicionales : if / elif / else
    - Repetitivas   : while, for
    - Manejo de errores: try / except
"""

import random
import string

# ---------------------------------------------------------------------------
# ESTRUCTURAS DE DATOS GLOBALES
# ---------------------------------------------------------------------------

# LISTA: estructura mutable que guarda el historial de contrasenas generadas
# durante la ejecucion del programa.
historial = []

# TUPLA: estructura inmutable que solo se usa como referencia informativa
# para sugerir al usuario longitudes de contrasena recomendadas.
longitudes_recomendadas = (8, 12, 16, 20)

# DICCIONARIO: agrupa los distintos conjuntos de caracteres disponibles
# para construir la contrasena. Cada "key" representa una categoria y cada
# "value" es la cadena de caracteres asociada a esa categoria.
caracteres = {
    "mayusculas": string.ascii_uppercase,
    "minusculas": string.ascii_lowercase,
    "numeros": string.digits,
    "simbolos": "!@#$%&*?"
}


def generar_password(longitud, mayusculas, numeros, simbolos):
    """
    Genera una contrasena segura combinando distintos conjuntos de
    caracteres del diccionario 'caracteres'.

    Parametros:
        longitud (int)   : cantidad total de caracteres de la contrasena.
        mayusculas (bool): incluir letras mayusculas.
        numeros (bool)   : incluir numeros.
        simbolos (bool)  : incluir simbolos especiales.

    Retorna:
        str: la contrasena generada.
    """

    password = []  # lista temporal que acumula los caracteres elegidos

    # Siempre incluir minusculas como base de la contrasena
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

    # Asegurar al menos una minuscula
    password.append(random.choice(caracteres["minusculas"]))

    # Completar el resto de caracteres de forma aleatoria (estructura repetitiva)
    while len(password) < longitud:
        password.append(random.choice(conjunto))

    # Mezclar para que no siga un patron predecible
    random.shuffle(password)

    return "".join(password)


def mostrar_historial():
    """Recorre la lista 'historial' y muestra todas las contrasenas generadas."""

    if len(historial) == 0:
        print("\nNo hay contrasenas generadas.")
        return

    print("\n===== HISTORIAL =====")

    # Estructura repetitiva 'for' recorriendo una lista
    for i, clave in enumerate(historial, start=1):
        print(f"{i}. {clave}")


def menu():
    """Funcion principal: controla el flujo del programa mediante un menu interactivo."""

    while True:  # estructura repetitiva principal del programa

        print("\n==============================")
        print(" GENERADOR DE CONTRASEÑAS ")
        print("==============================")
        print("Longitudes recomendadas:", longitudes_recomendadas)  # se muestra la tupla
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

            historial.append(password)  # se agrega el resultado a la lista

            print("\nContraseña generada:")
            print(password)

        elif opcion == "2":
            mostrar_historial()

        elif opcion == "3":
            print("\nGracias por usar el programa.")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    menu()
