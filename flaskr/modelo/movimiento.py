import unidecode

from datetime import datetime
from babel.dates import format_date
from babel.numbers import format_currency


class Movimiento:
    """Un movimiento del banco"""

    def __init__(self, linea):
        self.concepto = linea[0].strip()
        self._fecha_bruto = linea[1].strip()
        self._cantidad_bruto = float(linea[2])
        self.tipo = linea[3].strip()
        self.entidad = linea[4].strip()
        self.fecha = self.formatear_fecha(self._fecha_bruto)
        self.cantidad = self.formatear_cantidad(self._cantidad_bruto)

    def formatear_fecha(self, fecha_bruto):
        fecha = datetime.strptime(fecha_bruto, '%d-%m-%Y').date()
        return format_date(fecha, format='full', locale='es_ES')

    def formatear_cantidad(self, cantidad_bruto):
        return unidecode.unidecode(
            format_currency(cantidad_bruto, 'EUR', locale='es_ES'))

    def es_gasto(self):
        return self._cantidad_bruto < 0

    def es_ingreso(self):
        return not self.es_gasto()

    def como_dict(self):
        return {
            'concepto': self.concepto,
            'tipo': self.tipo,
            'entidad': self.entidad,
            'fecha': self.fecha,
            'cantidad': self.cantidad
        }
