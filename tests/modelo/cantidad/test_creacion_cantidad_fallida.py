import pytest
from modelo.cantidad import Cantidad


def test_cantidad_no_puede_estar_vacia():
    with pytest.raises(ValueError):
        Cantidad()


def test_cantidad_debe_ser_numerica():
    with pytest.raises(ValueError):
        Cantidad('mil doscientos')
