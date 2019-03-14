import json
import datetime

from modelo.movimiento import Movimiento
from modelo.concepto import Concepto
from modelo.cantidad import Cantidad
from modelo.fecha import Fecha
from modelo.tipo import Tipo
from modelo.entidad import Entidad


def test_formatear_como_json():
    """Formatear correctamente como json con todos los campos válidos"""

    # dado
    pasado = datetime.date(1999, 12, 31)
    movimiento = Movimiento(
        concepto=Concepto('el concepto'),
        fecha=Fecha(pasado),
        cantidad=Cantidad(1234.56),
        tipo=Tipo('el tipo'),
        entidad=Entidad('la entidad'))

    # cuando
    resultado = movimiento.como_json()

    # entonces
    assert resultado == generar_json({
        'concepto': 'el concepto',
        'fecha': 'viernes, 31 de diciembre de 1999',
        'cantidad': '1.234,56 EUR',
        'tipo': 'el tipo',
        'entidad': 'la entidad'
    })


def generar_json(diccionario):
    """Utilidad que genera un json usando un diccionario"""
    return json.dumps(diccionario)
