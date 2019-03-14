import json
from modelo.concepto import Concepto
from modelo.fecha import Fecha
from modelo.cantidad import Cantidad
from modelo.tipo import Tipo
from modelo.entidad import Entidad


class Movimiento:
    """Un movimiento del banco"""

    def __init__(self,
                 concepto=Concepto,
                 fecha=Fecha,
                 cantidad=Cantidad,
                 tipo=Tipo,
                 entidad=Entidad):
        self._concepto = concepto
        self._fecha = fecha
        self._cantidad = cantidad
        self._tipo = tipo
        self._entidad = entidad

    def como_json(self):
        """Devuelve una representación en formato json"""
        return json.dumps({
            'concepto': self._concepto.valor,
            'fecha': self._fecha.como_texto(),
            'cantidad': self._cantidad.como_texto(),
            'tipo': self._tipo.valor,
            'entidad': self._entidad.valor
        })
