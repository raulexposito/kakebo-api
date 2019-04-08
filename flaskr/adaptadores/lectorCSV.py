import csv

from modelo.movimiento import movimiento


class lectorCSV:
    @staticmethod
    def leer_movimientos(fichero):
        leidos = []
        saldo = 0
        with open(fichero, 'r') as ficheroCSV:
            lector = reversed(list(csv.reader(ficheroCSV)))
            for fila in lector:
                mov = movimiento(fila, saldo)
                leidos.append(mov)
                saldo += mov.cantidad
        return leidos
