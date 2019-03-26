from modelo.movimiento import Movimiento


def test_conversion_fecha():
    """Comprueba que la fecha se convierta a un formato largo"""

    # dado
    movimiento = Movimiento(['', '28-09-2018', 0, '', ''])

    # cuando
    resultado = movimiento.fecha

    # entonces
    assert resultado == 'viernes, 28 de septiembre de 2018'
