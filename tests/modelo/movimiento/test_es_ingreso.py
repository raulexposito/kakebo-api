from modelo.movimiento import movimiento


def test_es_ingreso():
    """Comprueba que la fecha se convierta a un formato largo"""

    # dado
    mov = movimiento(['', '28-09-2018', 0, '', ''], 0)

    # cuando
    resultado = mov.fecha

    # entonces
    assert resultado == 'viernes, 28 de septiembre de 2018'
