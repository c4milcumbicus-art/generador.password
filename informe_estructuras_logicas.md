# Informe técnico: Estructuras lógicas y repetitivas del Generador de Contraseñas

## 1. Introducción

Este informe describe cómo se aplicaron las estructuras lógicas (condicionales) y repetitivas (bucles) dentro del programa `main.py`, correspondiente al desarrollo del Generador de Contraseñas Seguras, en el marco del Paso 2 de la actividad.

## 2. Estructuras repetitivas (bucles)

### 2.1 Bucle `while` — Validación de la longitud

```python
longitud = 0
while longitud < 8:
    entrada = input("ingrese la longitud de la contraseña (mínimo 8): ")
    ...
```

Este bucle se repite **mientras** la variable `longitud` no alcance el mínimo permitido (8). El programa seguirá pidiendo un valor hasta que el usuario ingrese un número válido y suficiente. Esto evita que el programa continúe con una longitud inválida o demasiado corta.

### 2.2 Bucle `for` — Generación de caracteres

```python
for i in range(longitud - 4):
    caracter = random.choice(todos)
    contrasena += caracter
```

Este bucle se ejecuta una cantidad exacta de veces (la longitud solicitada, menos los 4 caracteres obligatorios ya agregados). En cada repetición se elige un carácter aleatorio del conjunto completo (`todos`) y se añade a la contraseña, hasta completar la longitud deseada.

## 3. Estructuras lógicas (condicionales)

### 3.1 Validación de tipo de dato

```python
if entrada.isdigit():
    longitud = int(entrada)
    if longitud < 8:
        print("La contraseña debe tener al menos 8 caracteres.\n")
else:
    print("Debe ingresar un número.\n")
```

- El primer `if` verifica que lo ingresado sea efectivamente un número (`isdigit()`), evitando errores si el usuario escribe letras o símbolos.
- El `if` anidado verifica que ese número cumpla con la longitud mínima requerida (8).
- El `else` maneja el caso de una entrada no numérica, informando al usuario del error.

Estas dos condiciones, combinadas con el bucle `while`, conforman el mecanismo de validación de entrada del programa.

## 4. Garantía de diversidad de caracteres

Como mejora aplicada al programa original, se incorporó una sección que asegura que la contraseña generada contenga **siempre** al menos un carácter de cada tipo disponible (mayúscula, minúscula, número y símbolo):

```python
contrasena += random.choice(mayusculas)
contrasena += random.choice(minusculas)
contrasena += random.choice(numeros)
contrasena += random.choice(simbolos)
```

Posteriormente, el orden de la contraseña se mezcla con `random.shuffle()` para que estos caracteres obligatorios no queden siempre en las primeras posiciones, manteniendo la aleatoriedad del resultado final.

## 5. Conclusión

El programa combina correctamente estructuras lógicas (`if`/`else`) y repetitivas (`while`, `for`) para validar la entrada del usuario y construir una contraseña aleatoria y segura, cumpliendo con los requisitos de la actividad: organización clara del código, comentarios explicativos y uso adecuado de condicionales y bucles.
