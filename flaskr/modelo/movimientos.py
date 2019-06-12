from utilidades.formateador import formateador
from utilidades.fecha import fecha

import itertools


class movimientos:
    """Un conjunto de movimientos"""

    def __init__(self, movimientos):
        self.movimientos = movimientos
        self._gastos = self._calcular_gastos(self.movimientos)
        self._ingresos = self._calcular_ingresos(self.movimientos)
        self._quedan = self._calcular_quedan()
        self._diferencia = self._gastos + self._ingresos

    def _calcular_gastos(self, movimientos):
        """devuelve la suma de todos los gastos"""
        return sum([mov._cantidad for mov in movimientos if mov.es_gasto()])

    def _calcular_ingresos(self, movimientos):
        """devuelve la suma de todos los ingresos"""
        return sum([mov._cantidad for mov in movimientos if mov.es_ingreso()])

    def _calcular_quedan(self):
        """devuelve el saldo que queda tras el ultimo movimiento"""
        return self.movimientos[0]._saldo

    def todos(self):
        """devuelve un nuevo conjunto con todos los movimientos"""
        return movimientos(list(reversed(self.movimientos)))

    def ultimos_meses(self, meses):
        """devuelve un nuevo conjunto con los movimientos realizados en los
        ultimos meses recibidos por parámetro"""
        return movimientos(
            list(
                reversed(
                    list(
                        itertools.dropwhile(
                            lambda movimiento: fecha.menor_de_x_meses(
                                meses, movimiento._fecha),
                            self.movimientos)))))

    @property
    def gastos(self):
        return abs(self._gastos)

    @property
    def ingresos(self):
        return self._ingresos

    @property
    def quedan(self):
        return formateador.cantidad(self._quedan)

    @property
    def diferencia(self):
        return formateador.cantidad(self._diferencia)
