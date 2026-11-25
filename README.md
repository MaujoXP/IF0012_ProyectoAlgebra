<<<<<<< HEAD
# IF0012 - Visualizador geométrico y calculadora de determinantes (Sarrus)

Aplicación de escritorio desarrollada en grupo por **Mauricio, Keylin y Letyavi**
para el curso IF0012. Integra, en una ventana con pestañas:

1. **Visualizador geométrico 2D** del primer cuadrante: puntos con clic, segmentos
   (dos clics), zoom con slider y dos paneles sincronizados.
2. **Calculadora de determinantes 3x3** por la regla de Sarrus, mostrando el
   procedimiento (productos principales y secundarios, sumas y resultado).

## Lenguaje y bibliotecas

- Python 3.9 o superior.
- Solo biblioteca estándar: `tkinter` / `ttk` (Canvas incluido).
- No se usan bibliotecas matemáticas externas para los procedimientos centrales.

## Estructura de archivos

```text
IF0012_Proyecto/
├── main.py                  # Punto de entrada
├── interfaz.py              # Ventana principal, pestañas e integración
├── geometria.py             # Datos geométricos y transformaciones
├── visualizador.py          # Canvas, eventos, dibujado y slider
├── determinantes.py         # Validación y regla de Sarrus
├── vista_determinantes.py   # Campos, procedimiento y resultados
└── README.md
```

| Archivo | Responsabilidad | Responsable |
|---|---|---|
| main.py | Punto de entrada | Mauricio |
| interfaz.py | Ventana principal, pestañas e integración | Mauricio |
| geometria.py | Datos geométricos y transformaciones | Keylin |
| visualizador.py | Canvas, eventos, dibujado y slider | Keylin |
| determinantes.py | Validación y regla de Sarrus | Letyavi |
| vista_determinantes.py | Campos, procedimiento y resultados | Letyavi |
| README.md | Documentación | Mauricio (todos aportan) |

## Ejecución

=======
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

>>>>>>> 63334caa392c1acb58b96afee82320f6bfc5b3ef
```bash
python main.py
```

<<<<<<< HEAD
Si `tkinter` no está instalado: en Windows y macOS viene con el instalador oficial
de Python; en Ubuntu/Debian use `sudo apt install python3-tk`.

## Módulos

- **Aplicacion (`interfaz.py`)**: crea la única raíz `Tk()`, un `ttk.Notebook` con
  dos pestañas e instancia `Visualizador(parent)` y `VistaDeterminantes(parent)`.
  No manipula los datos de esos componentes.
- **Geometria / Visualizador**: guarda los datos originales (no se mutan al hacer
  zoom). Panel izquierdo con factor 1 y panel derecho con factor `k` (0.5 a 3.0).
- **Determinantes / VistaDeterminantes**: la lógica devuelve un diccionario con
  productos, sumas y determinante; la vista solo lo muestra.

## Pruebas

Pruebas manuales acordadas (ver sección 10 del plan técnico):

- Visualizador: (2,3) con k=2 → (4,6); dos clics crean segmento; agregar no borra
  anteriores; zoom 0.5/1.0/2.0; clic fuera del primer cuadrante no registra; limpiar
  vacía listas y paneles.
- Determinantes: `[[2,1,3],[4,5,6],[7,8,9]]` → -9; identidad → 1; filas iguales → 0;
  `[[0,2,3],[4,0,6],[7,8,0]]` → 336; `[[-1,2,3],[4,-5,6],[7,8,-9]]` → -48;
  `[[1.5,2,0],[0,3,4],[5,0,2]]` → 9; campo vacío y texto inválido muestran mensaje.
- Integración: ambas pestañas, redimensionado de la ventana y ejecución desde `main.py`.

## Entrega

Domingo 29 de noviembre de 2026, 3:00 p. m.
=======
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
>>>>>>> 63334caa392c1acb58b96afee82320f6bfc5b3ef
