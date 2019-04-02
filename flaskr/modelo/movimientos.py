import csv
from modelo.movimiento import Movimiento


class Movimientos:
    """Un conjunto de movimientos"""

    def __init__(self, fichero):
        self.leidos = self._leer_movimientos(fichero)
        self.gastos = self._calcular_gastos(self.leidos)
        self.ingresos = self._calcular_ingresos(self.leidos)
        self.diferencia = self.gastos + self.ingresos

    def _leer_movimientos(self, fichero):
        leidos = []
        with open(fichero) as ficheroCSV:
            lector = csv.reader(ficheroCSV)
            for fila in lector:
                leidos.append(Movimiento(fila))
        return leidos

    def _calcular_gastos(self, leidos):
        total = 0
        for movimiento in leidos:
            if (movimiento.es_gasto()):
                total = total + movimiento._cantidad_bruto
        return total

    def _calcular_ingresos(self, leidos):
        total = 0
        for movimiento in leidos:
            if (movimiento.es_ingreso()):
                total = total + movimiento._cantidad_bruto
        return total

    def como_dict(self):
        leidos = []
        for leido in self.leidos:
            leidos.append(leido.como_dict())

        return {
            'gastos': self.gastos,
            'ingresos': self.ingresos,
            'diferencia': self.diferencia,
            'leidos': leidos
        }
