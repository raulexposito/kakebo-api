from datetime import date


class Fecha:
    """El día en el que se realizó el movimiento"""

    def __new__(cls, valor=date.today()):
        if valor > date.today():
            raise ValueError('La fecha no puede ser futura')
        instance = super(Fecha, cls).__new__(cls)
        instance.__init__(valor)
        return instance

    def __init__(self, valor=date.today()):
        self._valor = valor

    def como_texto(self):
        """Devuelve una representación con el formato dia-mes-año"""
        return self._valor.strftime('%d-%m-%Y')
