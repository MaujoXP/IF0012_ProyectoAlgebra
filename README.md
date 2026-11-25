# Proyecto IF0012 - Álgebra Lineal

## Descripción

Aplicación de escritorio desarrollada en Python como parte del proyecto del curso IF0012. El programa integra herramientas de visualización geométrica en un plano cartesiano y cálculo de determinantes de matrices de orden 3x3.

La aplicación permite representar puntos y segmentos en el primer cuadrante del plano cartesiano, visualizar transformaciones de escala y calcular determinantes mediante la regla de Sarrus, mostrando el procedimiento utilizado para obtener el resultado.

## Funcionalidades

### Visualizador geométrico
- Representación de puntos en el primer cuadrante del plano cartesiano.
- Creación y visualización de segmentos entre puntos.
- Aplicación de transformaciones de escala.
- Visualización simultánea de los elementos originales y transformados.
- Ajuste de escala mediante un control deslizante.
- Limpieza del área de visualización.

### Calculadora de determinantes
- Ingreso de matrices de orden 3x3.
- Validación de los valores ingresados.
- Cálculo de determinantes mediante la regla de Sarrus.
- Visualización de los productos diagonales principales y secundarios.
- Presentación del procedimiento y resultado final.

## Tecnologías utilizadas

- **Python:** Lenguaje de programación utilizado para el desarrollo.
- **Tkinter:** Biblioteca utilizada para la creación de la interfaz gráfica.
- **ttk:** Componentes gráficos adicionales de Tkinter.
- **Canvas:** Componente utilizado para la representación gráfica del plano cartesiano y los elementos geométricos.

## Estructura del proyecto

```text
IF0012_Proyecto/
│
├── main.py
├── interfaz.py
├── geometria.py
├── visualizador.py
├── determinantes.py
├── vista_determinantes.py
└── README.md
```

| Archivo | Descripción |
|---|---|
| `main.py` | Punto de entrada de la aplicación. |
| `interfaz.py` | Configuración de la ventana principal y organización de las funcionalidades. |
| `geometria.py` | Gestión de puntos, segmentos y transformaciones geométricas. |
| `visualizador.py` | Interfaz y representación gráfica del plano cartesiano. |
| `determinantes.py` | Validación y cálculo de determinantes mediante la regla de Sarrus. |
| `vista_determinantes.py` | Interfaz de ingreso de matrices y presentación de resultados. |
| `README.md` | Documentación general del proyecto. |

## Requisitos

- Python 3.10 o superior.
- Tkinter, incluido normalmente en las instalaciones estándar de Python.

No se requiere la instalación de bibliotecas matemáticas externas para las funcionalidades principales del programa.

## Ejecución

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta raíz del proyecto.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 main.py
```

## Integrantes

- Mauricio
- Keylin
- Letyavi

## Curso

IF0012 - Álgebra Lineal

**Proyecto académico.**
