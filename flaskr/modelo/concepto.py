class Concepto:
    """El motivo del movimiento"""

    def __new__(cls, valor=''):
        if valor.strip() == '':
            raise ValueError('El concepto no puede estar vacío')
        instance = super(Concepto, cls).__new__(cls)
        instance.__init__(valor)
        return instance

    def __init__(self, valor=''):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
