from utilidades.formateador import formateador


class movimiento:
    """Un movimiento del banco"""

    def __init__(self, linea, saldo):
        self.concepto = linea[0].strip()
        self._fecha = linea[1].strip()
        self.fecha = formateador.fecha(self._fecha)
        self._cantidad = float(linea[2])
        self.cantidad = formateador.cantidad(self._cantidad)
        self.tipo = linea[3].strip()
        self.entidad = linea[4].strip()
        self._saldo = saldo + self._cantidad
        self.saldo = formateador.cantidad(self._saldo)

    def es_gasto(self):
        return self._cantidad < 0

    def es_ingreso(self):
        return not self.es_gasto()
