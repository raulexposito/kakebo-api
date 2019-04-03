import unidecode

from datetime import datetime
from babel.dates import format_date
from babel.numbers import format_currency


class Formateador:
    @staticmethod
    def fecha(fecha_bruto):
        fecha = datetime.strptime(fecha_bruto, '%d-%m-%Y').date()
        return format_date(fecha, format='full', locale='es_ES')

    @staticmethod
    def cantidad(cantidad_bruto):
        return unidecode.unidecode(
            format_currency(cantidad_bruto, 'EUR', locale='es_ES'))
