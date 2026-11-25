"""Vista de la calculadora de determinantes (responsable: LETYAVI).

ESTE ES UN ESQUELETO TEMPORAL creado por Mauricio para que la integración
funcione desde el día 1. Letyavi: reemplaza el contenido manteniendo el nombre
de la clase y la firma  VistaDeterminantes(parent)  (ver TAREAS_LETYAVI en el
espacio de trabajo y la sección 5 del plan técnico).

Reglas: usar el `parent` recibido, NO crear Tk(), y empaquetar el contenido
con self.frame.pack(fill="both", expand=True). La vista NO calcula: llama a
Determinantes.calcular_determinante(matriz) y solo muestra el diccionario.
"""
import tkinter as tk
from tkinter import ttk

# from determinantes import Determinantes   # TODO (Letyavi): descomentar al tener determinantes.py


class VistaDeterminantes:
    def __init__(self, parent):
        self.parent = parent
        # TODO (Letyavi): self.logica = Determinantes()
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill="both", expand=True)
        self.crear_interfaz()

    def crear_interfaz(self):
        # TODO (Letyavi): 9 campos Entry, botones Calcular/Limpiar, áreas de resultados
        ttk.Label(
            self.frame,
            text="Calculadora de determinantes (Sarrus) - PENDIENTE (Letyavi)",
            font=("Segoe UI", 14),
        ).pack(expand=True)

    def obtener_datos(self):
        pass  # TODO

    def calcular(self):
        pass  # TODO

    def mostrar_resultado(self, resultado):
        pass  # TODO

    def mostrar_matriz(self, matriz):
        pass  # TODO

    def limpiar(self):
        pass  # TODO

    def dibujar_sarrus(self, matriz):
        pass  # TODO (opcional, al final)
