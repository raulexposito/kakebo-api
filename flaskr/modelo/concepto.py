class Concepto:
    """El motivo del movimiento"""

    def __init__(self, valor=''):
        self.validar(valor)

        self._valor = valor

    @classmethod
    def validar(cls, valor):
        if valor.strip() == '':
            raise ValueError('El concepto no puede estar vacio')

    @property
    def valor(self):
        return self._valor
