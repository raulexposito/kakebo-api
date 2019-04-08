from datetime import datetime
from dateutil.relativedelta import relativedelta


class fecha:
    @staticmethod
    def cadena_a_fecha(cadena):
        return datetime.strptime(cadena, '%d-%m-%Y').date()

    @staticmethod
    def fecha_hace_x_meses(meses):
        return (datetime.now() - relativedelta(months=meses)).date()

    @staticmethod
    def menor_de_x_meses(meses, cadena):
        return fecha.fecha_hace_x_meses(meses) > fecha.cadena_a_fecha(cadena)
