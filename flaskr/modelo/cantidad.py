from babel.numbers import format_currency
import unidecode


class Cantidad:
    """El importe del movimiento"""

    def __new__(cls, valor=None):
        if valor is None:
            raise ValueError('La cantidad no puede estar vacía')
        elif not isinstance(valor, (int, float)):
            raise ValueError('La cantidad debe ser un número')
        instance = super(Cantidad, cls).__new__(cls)
        instance.__init__(valor)
        return instance

    def __init__(self, valor=None):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def como_texto(self):
        return unidecode.unidecode(
            format_currency(self._valor, 'EUR', locale='es_ES'))
