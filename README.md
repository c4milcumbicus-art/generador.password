# SecureGen — Generador Inteligente de Contraseñas Seguras

Proyecto Integrador · UIDE · Asignatura: Programación (Unidades 1-4: lógica de programación, estructuras de control, funciones y **estructuras de datos**)

---

## 1. Integrantes

- [Nombre completo del/la estudiante] — [correo institucional]
- *(Agregar un punto por cada integrante si el proyecto se realizó en grupo)*

## 2. Fecha

27 de junio de 2026 *(actualizar con la fecha real de entrega)*

## 3. Objetivo del sistema

Desarrollar una aplicación de consola en Python que permita a cualquier persona **generar contraseñas seguras y personalizadas**, como respuesta directa a uno de los impactos más relevantes de las nuevas tecnologías en la sociedad actual: el aumento de los riesgos de ciberseguridad y el robo de identidad digital provocado por el uso de contraseñas débiles o repetidas.

El sistema integra los contenidos vistos durante las cuatro unidades del curso:

| Unidad | Contenido aplicado en el proyecto |
|---|---|
| 1 | Lógica de programación y sintaxis básica de Python |
| 2 | Estructuras de control condicionales (`if` / `elif` / `else`) |
| 3 | Estructuras de control repetitivas (`while`, `for`) y manejo de errores (`try`/`except`) |
| 4 | **Estructuras de datos** (tupla, lista, diccionario) y **funciones** con parámetros y retorno |

## 4. Descripción de funcionalidades

| # | Funcionalidad | Descripción |
|---|---|---|
| 1 | Generar contraseña | Solicita la longitud deseada (mínimo 8) y si se desean incluir mayúsculas, números y símbolos; genera una contraseña aleatoria y la guarda en el historial. |
| 2 | Ver historial | Muestra todas las contraseñas generadas durante la sesión actual. |
| 3 | Salir | Finaliza la ejecución del programa de forma controlada. |

**Estructuras de datos utilizadas (`main.py`):**

- `caracteres` → **diccionario** que agrupa los conjuntos de caracteres (mayúsculas, minúsculas, números, símbolos).
- `historial` → **lista** mutable que almacena cada contraseña generada.
- `longitudes_recomendadas` → **tupla** inmutable con valores sugeridos de longitud (8, 12, 16, 20).
- `generar_password()`, `mostrar_historial()`, `menu()` → **funciones** con parámetros y valores de retorno que organizan la lógica del programa.

## 5. Estructura del repositorio

```
proyecto-integrador/
│
├── main.py                          # Código fuente completo del sistema
├── README.md                        # Este archivo
│
├── diagramas/                       # Diagramas de funcionalidad y arquitectura
│   ├── diagrama_flujo.png
│   ├── diagrama_casos_uso.png
│   └── diagrama_arquitectura.png
│
├── docs/                            # Documento del proyecto y guion del video
│   ├── Documento_Proyecto_Integrador.docx
│   └── Guion_Video_Demostrativo.docx
│
└── presentacion/                    # Presentación final
    └── Presentacion_SecureGen.pptx
```

## 6. Cómo ejecutar el programa

Requisitos: Python 3.8 o superior (no requiere librerías externas).

```bash
git clone <url-de-este-repositorio>
cd proyecto-integrador
python3 main.py
```

Sigue las instrucciones del menú en consola para generar contraseñas o consultar el historial.

## 7. Cronograma de desarrollo (semanas 1 a 8)

| Semana | Actividad |
|---|---|
| 1 | Planificación del proyecto: definición del problema y alcance |
| 2 | Investigación sobre impacto tecnológico y ciberseguridad |
| 3 | Diseño de diagramas de funcionalidad (casos de uso y flujo) |
| 4 | Diseño de la arquitectura del sistema |
| 5 | Desarrollo del código base (estructuras condicionales y repetitivas) |
| 6 | Integración de estructuras de datos y funciones (Unidad 4) |
| 7 | Pruebas, control de versiones en GitHub y documentación |
| 8 | Elaboración del documento final, presentación y video demostrativo |

## 8. Herramientas utilizadas

- **Python 3** — lenguaje de programación
- **Git / GitHub** — control de versiones
- **Visual Studio Code** — entorno de desarrollo
- **PowerPoint** — presentación final
