from modelo.movimiento import Movimiento


def test_limpiar_tipo():
    """Comprueba que el tipo se recupera sin espacios en blanco"""

    # dado
    movimiento = Movimiento(['', '28-09-2018', 0, '\t\ttipo\n', ''])

    # cuando
    resultado = movimiento.tipo

    # entonces
    assert resultado == 'tipo'
