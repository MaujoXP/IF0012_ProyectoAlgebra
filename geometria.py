"""Datos geométricos y transformaciones (responsable: KEYLIN).

ESQUELETO con las firmas acordadas. Sin GUI ni Tkinter.
Formato de datos:  punto = (x, y)   segmento = ((x1, y1), (x2, y2))
"""


class Geometria:
    def __init__(self):
        self.puntos = []
        self.segmentos = []
        self.factor_escala = 1.0

    def agregar_punto(self, x, y):
        """Registrar el punto si x >= 0 y y >= 0. Devolver True/False."""
        raise NotImplementedError  # TODO (Keylin)

    def agregar_segmento(self, punto1, punto2):
        """Guardar los dos extremos como un segmento."""
        raise NotImplementedError  # TODO (Keylin)

    def aplicar_escala(self, x, y, factor):
        """Devolver (x*factor, y*factor)."""
        raise NotImplementedError  # TODO (Keylin)

    def obtener_puntos(self):
        raise NotImplementedError  # TODO (Keylin)

    def obtener_segmentos(self):
        raise NotImplementedError  # TODO (Keylin)

    def limpiar(self):
        raise NotImplementedError  # TODO (Keylin)

    def establecer_escala(self, factor):
        raise NotImplementedError  # TODO (Keylin)
