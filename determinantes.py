"""Lógica del determinante 3x3 por regla de Sarrus (responsable: LETYAVI).

ESQUELETO con las firmas acordadas. Sin GUI ni Tkinter; no usar bibliotecas
matemáticas externas (nada de numpy/sympy).

matriz = [[a, b, c], [d, e, f], [g, h, i]]
"""


class Determinantes:
    def validar_matriz(self, datos):
        """Nueve campos, no vacíos y numéricos. Devolver (ok, mensaje)."""
        raise NotImplementedError  # TODO (Letyavi)

    def convertir_matriz(self, datos):
        """Convertir los nueve datos a matriz 3x3 de floats."""
        raise NotImplementedError  # TODO (Letyavi)

    def calcular_productos(self, matriz):
        """Seis productos: P1=a*e*i, P2=b*f*g, P3=c*d*h, S1=c*e*g, S2=b*d*i, S3=a*f*h."""
        raise NotImplementedError  # TODO (Letyavi)

    def sumar_principales(self, productos):
        raise NotImplementedError  # TODO (Letyavi)

    def sumar_secundarias(self, productos):
        raise NotImplementedError  # TODO (Letyavi)

    def calcular_determinante(self, matriz):
        """Devolver el diccionario acordado:
        {"productos_principales": [P1,P2,P3], "productos_secundarios": [S1,S2,S3],
         "suma_principal": SP, "suma_secundaria": SS, "determinante": D}"""
        raise NotImplementedError  # TODO (Letyavi)
