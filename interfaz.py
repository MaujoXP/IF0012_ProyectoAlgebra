"""Ventana principal, pestañas e integración de los módulos (responsable: Mauricio).

Esta clase únicamente instancia los componentes de Keylin (Visualizador) y
de Letyavi (VistaDeterminantes) dentro de las pestañas. No manipula sus
datos ni crea otras raíces Tk().
"""
import tkinter as tk
from tkinter import ttk

from visualizador import Visualizador
from vista_determinantes import VistaDeterminantes


class Aplicacion:
    TITULO = "IF0012 - Visualizador geométrico y Determinantes (Sarrus)"
    ANCHO = 1100
    ALTO = 720
    MIN_ANCHO = 900
    MIN_ALTO = 600

    def __init__(self):
        self.ventana = tk.Tk()
        self.configurar_ventana()
        self.crear_pestanas()
        self.integrar_visualizador()
        self.integrar_determinantes()

    def configurar_ventana(self):
        """Título, tamaño inicial (centrado), tamaño mínimo y redimensionado."""
        self.ventana.title(self.TITULO)
        x = (self.ventana.winfo_screenwidth() - self.ANCHO) // 2
        y = (self.ventana.winfo_screenheight() - self.ALTO) // 2
        self.ventana.geometry(f"{self.ANCHO}x{self.ALTO}+{max(x, 0)}+{max(y, 0)}")
        self.ventana.minsize(self.MIN_ANCHO, self.MIN_ALTO)
        self.ventana.resizable(True, True)

    def crear_pestanas(self):
        """ttk.Notebook con dos pestañas; cada una es un contenedor Frame
        que se expande al redimensionar la ventana."""
        self.notebook = ttk.Notebook(self.ventana)
        self.notebook.pack(fill="both", expand=True, padx=6, pady=6)

        self.pestana_visualizador = ttk.Frame(self.notebook)
        self.pestana_determinantes = ttk.Frame(self.notebook)
        self.notebook.add(self.pestana_visualizador, text="Visualizador geométrico")
        self.notebook.add(self.pestana_determinantes, text="Determinantes 3x3 (Sarrus)")

    def integrar_visualizador(self):
        """Instancia el Visualizador (Keylin) dentro de la primera pestaña."""
        self.visualizador = Visualizador(self.pestana_visualizador)

    def integrar_determinantes(self):
        """Instancia VistaDeterminantes (Letyavi) dentro de la segunda pestaña."""
        self.vista_determinantes = VistaDeterminantes(self.pestana_determinantes)

    def iniciar(self):
        self.ventana.mainloop()
