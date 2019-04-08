import unidecode

from babel.dates import format_date
from babel.numbers import format_currency
from utilidades.fecha import fecha


class formateador:
    @staticmethod
    def fecha(fecha_bruto):
        return format_date(
            fecha.cadena_a_fecha(fecha_bruto), format='full', locale='es_ES')

    @staticmethod
    def cantidad(cantidad_bruto):
        return unidecode.unidecode(
            format_currency(cantidad_bruto, 'EUR', locale='es_ES'))
