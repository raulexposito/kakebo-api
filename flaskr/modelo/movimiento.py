from utilidades.formateador import formateador


class movimiento:
    """Un movimiento del banco"""

    def __init__(self, linea, saldo):
        self.concepto = linea[0].strip()
        self.fecha = linea[1].strip()
        self.cantidad = float(linea[2])
        self.tipo = linea[3].strip()
        self.entidad = linea[4].strip()
        self.saldo = saldo

    def es_gasto(self):
        return self.cantidad < 0

    def es_ingreso(self):
        return not self.es_gasto()

    def como_dict(self):
        return {
            'concepto': self.concepto,
            'tipo': self.tipo,
            'entidad': self.entidad,
            'fecha': formateador.fecha(self.fecha),
            'cantidad': formateador.cantidad(self.cantidad),
            'saldo': formateador.cantidad(self.saldo)
        }
