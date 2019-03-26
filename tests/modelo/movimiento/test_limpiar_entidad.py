from modelo.movimiento import Movimiento


def test_limpiar_entidad():
    """Comprueba que la entidad se recupera sin espacios en blanco"""

    # dado
    movimiento = Movimiento(['', '28-09-2018', 0, '', '\n\tentidad   '])

    # cuando
    resultado = movimiento.entidad

    # entonces
    assert resultado == 'entidad'
