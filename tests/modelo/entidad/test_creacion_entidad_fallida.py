import pytest
from modelo.entidad import Entidad


def test_entidad_no_puede_estar_vacia():
    with pytest.raises(ValueError):
        Entidad()


def test_entidad_no_acepta_string_vacios():
    with pytest.raises(ValueError):
        Entidad('')


def test_entidad_no_acepta_strings_solo_con_blancos():
    with pytest.raises(ValueError):
        Entidad('       ')
