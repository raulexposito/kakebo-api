import csv
from modelo.movimiento import Movimiento
from utilidades.formateador import Formateador


class Movimientos:
    """Un conjunto de movimientos"""

    def __init__(self, fichero):
        self.leidos = self._leer_movimientos(fichero)
        self.gastos = self._calcular_gastos(self.leidos)
        self.ingresos = self._calcular_ingresos(self.leidos)
        self.diferencia = self.gastos + self.ingresos

    def _leer_movimientos(self, fichero):
        leidos = []
        saldo = 0
        with open(fichero, 'r') as ficheroCSV:
            lector = reversed(list(csv.reader(ficheroCSV)))
            for fila in lector:
                movimiento = Movimiento(fila, saldo)
                leidos.append(movimiento)
                saldo += movimiento.cantidad
        return leidos

    def _calcular_gastos(self, leidos):
        return sum([mov.cantidad for mov in leidos if mov.es_gasto()])

    def _calcular_ingresos(self, leidos):
        return sum([mov.cantidad for mov in leidos if mov.es_ingreso()])

    def como_dict(self):
        return {
            'gastos': Formateador.cantidad(self.gastos),
            'ingresos': Formateador.cantidad(self.ingresos),
            'diferencia': Formateador.cantidad(self.diferencia),
            'leidos': self._leidos_como_dict()
        }

    def _leidos_como_dict(self):
        leidos = []
        for leido in self.leidos:
            leidos.append(leido.como_dict())
        return leidos
