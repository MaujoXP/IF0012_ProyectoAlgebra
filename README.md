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

```bash
python main.py
```

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
