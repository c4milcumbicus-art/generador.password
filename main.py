import random
import string

print("--- Generador de contraseña ---")

# --- Validación de la longitud ingresada por el usuario ---
longitud = 0
while longitud < 8:
    entrada = input("ingrese la longitud de la contraseña (mínimo 8): ")
    if entrada.isdigit():
        longitud = int(entrada)
        if longitud < 8:
            print("La contraseña debe tener al menos 8 caracteres.\n")
    else:
        print("Debe ingresar un número.\n")

# --- Conjuntos de caracteres disponibles ---
mayusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = "!@#$%&*?"

todos = mayusculas + minusculas + numeros + simbolos

# --- Garantizamos al menos un caracter de cada tipo ---
# (así la contraseña siempre es variada, no solo letras o solo números)
contrasena = ""
contrasena += random.choice(mayusculas)
contrasena += random.choice(minusculas)
contrasena += random.choice(numeros)
contrasena += random.choice(simbolos)

# --- Completamos el resto de la longitud con caracteres aleatorios ---
for i in range(longitud - 4):
    caracter = random.choice(todos)
    contrasena += caracter

# --- Mezclamos el orden para que los 4 obligatorios no queden siempre al inicio ---
lista_contrasena = list(contrasena)
random.shuffle(lista_contrasena)
contrasena = "".join(lista_contrasena)

print("\n¡Contraseña creada con éxito!")
print("Su contraseña es:", contrasena)
