class Entidad:
    """La entidad del movimiento"""

    def __new__(cls, valor=''):
        if valor.strip() == '':
            raise ValueError('La entidad no puede estar vacía')
        instance = super(Entidad, cls).__new__(cls)
        instance.__init__(valor)
        return instance

    def __init__(self, valor=''):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
