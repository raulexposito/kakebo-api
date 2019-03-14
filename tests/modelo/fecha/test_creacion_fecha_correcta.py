import datetime

from datetime import date
from modelo.fecha import Fecha
from babel.dates import format_date


def test_fecha_por_defecto_es_hoy():

    # dado
    fecha = Fecha()

    # cuando
    resultado = fecha.como_texto()

    # entonces
    assert resultado == hoy_como_texto()


def test_fechas_pasadas_pueden_ser_creadas():

    # dado
    pasado = datetime.date(1999, 12, 31)
    pasado_como_texto = "viernes, 31 de diciembre de 1999"
    fecha = Fecha(pasado)

    # cuando
    resultado = fecha.como_texto()

    # entonces
    assert resultado == pasado_como_texto


def hoy_como_texto():
    """Convierte una fecha completa en texto"""
    return format_date(date.today(), format='full', locale='es_ES')
