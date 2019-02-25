import pytest
from modelo.concepto import Concepto


def test_concepto_no_puede_estar_vacio():
    with pytest.raises(ValueError):
        Concepto()


def test_concepto_no_acepta_string_vacios():
    with pytest.raises(ValueError):
        Concepto('')


def test_concepto_no_acepta_strings_solo_con_blancos():
    with pytest.raises(ValueError):
        Concepto('       ')
