import pytest
import datetime

from modelo.fecha import Fecha


def test_fechas_futuras_no_pueden_ser_creadas():

    # dado
    futuro = datetime.date(2999, 12, 31)

    # entonces
    with pytest.raises(ValueError):
        Fecha(futuro)
