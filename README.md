# Generador de Contraseñas Seguras

Programa de consola desarrollado en **Python** que genera contraseñas aleatorias y seguras a partir de la longitud indicada por el usuario.

## Descripción

El programa solicita al usuario la longitud deseada para la contraseña (mínimo 8 caracteres) y genera una contraseña aleatoria que combina:

- Letras mayúsculas (A-Z)
- Letras minúsculas (a-z)
- Números (0-9)
- Símbolos especiales (`!@#$%&*?`)

Para garantizar que la contraseña sea realmente segura y variada, el programa asegura que **siempre** contenga al menos un carácter de cada tipo, y luego mezcla el orden de todos los caracteres de forma aleatoria.

## Funcionalidades principales

- Validación de la entrada del usuario (rechaza texto no numérico).
- Validación de longitud mínima (8 caracteres), repitiendo la solicitud hasta recibir un valor válido.
- Generación de contraseñas con diversidad garantizada de caracteres.
- Mezcla aleatoria del resultado final con `random.shuffle`.

## Estructuras lógicas y repetitivas utilizadas

| Estructura | Uso en el programa |
|---|---|
| `while` | Repite la solicitud de la longitud hasta que el usuario ingrese un número válido (≥ 8). |
| `if / else` | Valida si la entrada es un número y si cumple con la longitud mínima. |
| `for` | Recorre la cantidad de caracteres restantes para completar la longitud solicitada. |

## Tecnologías y herramientas

- **Lenguaje:** Python 3
- **Librerías:** `random`, `string` (ambas de la librería estándar, no requieren instalación)
- **IDE/Editor:** Visual Studio Code
- **Control de versiones:** Git y GitHub

## Cómo ejecutar el programa

1. Asegúrate de tener Python 3 instalado:
   ```bash
   python3 --version
   ```
2. Clona este repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-repositorio>
   ```
3. Ejecuta el programa:
   ```bash
   python3 main.py
   ```
4. Ingresa la longitud deseada cuando se te solicite (mínimo 8) y presiona Enter.

## Diagrama de flujo

El diagrama de flujo con la lógica completa del programa se encuentra en [`diagrama_flujo.png`](diagrama_flujo.png).

## Capturas de funcionamiento

En la carpeta [`capturas/`](capturas/) se incluyen evidencias de ejecución del programa:

- `captura_01_caso_basico.png`: generación de una contraseña con la longitud mínima (8).
- `captura_02_validaciones.png`: comportamiento del programa ante una entrada inválida (texto) y una longitud insuficiente (5), antes de aceptar un valor correcto.
- `captura_03_contrasena_larga.png`: generación de una contraseña más larga (16 caracteres).

## Documentos adicionales

En la carpeta [`documentos/`](documentos/) se incluye un informe con el detalle de las estructuras lógicas y repetitivas implementadas en el código.

## Estructura del repositorio

```
.
├── main.py                  # Código fuente del generador de contraseñas
├── README.md                # Este archivo
├── diagrama_flujo.png       # Diagrama de flujo del programa
├── capturas/                # Evidencias de ejecución del programa
└── documentos/               # Informes y documentación adicional
```

## Autor

Proyecto desarrollado como parte de la actividad de análisis e implementación de software.
