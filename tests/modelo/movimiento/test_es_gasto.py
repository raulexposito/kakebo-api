from modelo.movimiento import movimiento


def test_es_gasto():
    """Comprueba que la cantidad se convierta a un formato largo"""

    # dado
    mov = movimiento(['', '28-09-2018', '10203.04', '', ''], 0)

    # cuando
    resultado = mov.cantidad

    # entonces
    assert resultado == '10.203,04 EUR'
