import json
import datetime

from modelo.movimiento import Movimiento
from modelo.concepto import Concepto
from modelo.fecha import Fecha


def test_formatear_como_json():
    """Formatear correctamente como json con todos los campos válidos"""

    # dado
    pasado = datetime.date(1999, 12, 31)
    movimiento = Movimiento(
        concepto=Concepto('el concepto'),
        fecha=Fecha(pasado),
        cantidad='1000',
        tipo='el tipo',
        entidad='la entidad')

    # cuando
    resultado = movimiento.como_json()

    # entonces
    assert resultado == generar_json({
        'concepto': 'el concepto',
        'fecha': '31-12-1999',
        'cantidad': '1000',
        'tipo': 'el tipo',
        'entidad': 'la entidad'
    })


def generar_json(diccionario):
    """Utilidad que genera un json usando un diccionario"""
    return json.dumps(diccionario)
