import pytest
from modelo.tipo import Tipo


def test_tipo_no_puede_estar_vacio():
    with pytest.raises(ValueError):
        Tipo()


def test_tipo_no_acepta_string_vacios():
    with pytest.raises(ValueError):
        Tipo('')


def test_tipo_no_acepta_strings_solo_con_blancos():
    with pytest.raises(ValueError):
        Tipo('       ')
