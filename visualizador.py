"""Visualizador geométrico 2D (responsable: KEYLIN).

ESTE ES UN ESQUELETO TEMPORAL creado por Mauricio para que la integración
funcione desde el día 1. Keylin: reemplaza el contenido manteniendo el nombre
de la clase y la firma  Visualizador(parent)  (ver TAREAS_KEYLIN en el espacio
de trabajo y la sección 4 del plan técnico).

Reglas: usar el `parent` recibido, NO crear Tk(), y empaquetar el contenido
con self.frame.pack(fill="both", expand=True).
"""
import tkinter as tk
from tkinter import ttk

# from geometria import Geometria   # TODO (Keylin): descomentar al tener geometria.py


class Visualizador:
    def __init__(self, parent):
        self.parent = parent
        # TODO (Keylin): self.geometria = Geometria()
        # TODO (Keylin): self.punto_pendiente = None
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill="both", expand=True)
        self.crear_interfaz()

    def crear_interfaz(self):
        # TODO (Keylin): dos Canvas, slider (50-300), etiqueta de escala, botón Limpiar
        ttk.Label(
            self.frame,
            text="Visualizador geométrico - PENDIENTE (Keylin)",
            font=("Segoe UI", 14),
        ).pack(expand=True)

    def registrar_clic(self, event):
        pass  # TODO

    def convertir_a_coordenadas(self, event):
        pass  # TODO

    def convertir_a_pantalla(self, x, y, factor):
        pass  # TODO

    def dibujar_ejes(self, canvas):
        pass  # TODO

    def dibujar_puntos(self, canvas, puntos, factor):
        pass  # TODO

    def dibujar_segmentos(self, canvas, segmentos, factor):
        pass  # TODO

    def redibujar(self):
        pass  # TODO

    def cambiar_zoom(self, valor):
        pass  # TODO

    def limpiar_dibujo(self):
        pass  # TODO

    def gestionar_segmento(self, punto):
        pass  # TODO
