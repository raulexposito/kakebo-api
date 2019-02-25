from datetime import date


class Fecha:
    """El día en el que se realizó el movimiento"""

    def __init__(self, valor=date.today()):
        self.validar(valor)

        self._valor = valor

    @classmethod
    def validar(cls, valor):
        if valor > date.today():
            raise ValueError('La fecha no puede ser futura')

    def como_texto(self):
        """Devuelve una representación con el formato dia-mes-año"""
        return self._valor.strftime('%d-%m-%Y')
