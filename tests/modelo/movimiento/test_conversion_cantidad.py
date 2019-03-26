from modelo.movimiento import Movimiento


def test_convesion_cantidad():
    """Comprueba que la cantidad se convierta a un formato largo"""

    # dado
    movimiento = Movimiento(['', '28-09-2018', '10203.04', '', ''])

    # cuando
    resultado = movimiento.cantidad

    # entonces
    assert resultado == '10.203,04 EUR'
