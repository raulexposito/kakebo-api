class Tipo:
    """El tipo del movimiento"""

    def __new__(cls, valor=''):
        if valor.strip() == '':
            raise ValueError('El tipo no puede estar vacío')
        instance = super(Tipo, cls).__new__(cls)
        instance.__init__(valor)
        return instance

    def __init__(self, valor=''):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
