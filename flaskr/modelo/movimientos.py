from utilidades.formateador import formateador
from utilidades.fecha import fecha

import itertools


class movimientos:
    """Un conjunto de movimientos"""

    def __init__(self, movimientos):
        self.movimientos = movimientos
        self.gastos = self._calcular_gastos(self.movimientos)
        self.ingresos = self._calcular_ingresos(self.movimientos)
        self.diferencia = self.gastos + self.ingresos
        self.quedan = self._calcular_quedan()

    def _calcular_gastos(self, leidos):
        return sum([mov.cantidad for mov in leidos if mov.es_gasto()])

    def _calcular_ingresos(self, leidos):
        return sum([mov.cantidad for mov in leidos if mov.es_ingreso()])

    def _calcular_quedan(self):
        return self.movimientos[-1].saldo + self.movimientos[-1].cantidad

    def todos(self):
        return movimientos(self.movimientos)

    def ultimos_meses(self, meses):
        return movimientos(
            list(
                itertools.dropwhile(
                    lambda movimiento: fecha.menor_de_x_meses(
                        meses, movimiento.fecha), self.movimientos)))

    def como_dict(self):
        return {
            'gastos': formateador.cantidad(self.gastos),
            'ingresos': formateador.cantidad(self.ingresos),
            'diferencia': formateador.cantidad(self.diferencia),
            'quedan': formateador.cantidad(self.quedan),
            'leidos': self._leidos_como_dict()
        }

    def _leidos_como_dict(self):
        leidos = []
        for leido in self.movimientos:
            leidos.append(leido.como_dict())
        return leidos
