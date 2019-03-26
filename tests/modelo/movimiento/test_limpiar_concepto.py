from modelo.movimiento import Movimiento


def test_limpiar_concepto():
    """Comprueba que el concepto se recupera sin espacios en blanco"""

    # dado
    movimiento = Movimiento([' concepto\t', '28-09-2018', 0, '', ''])

    # cuando
    resultado = movimiento.concepto

    # entonces
    assert resultado == 'concepto'
