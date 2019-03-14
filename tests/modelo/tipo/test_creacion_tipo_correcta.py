from modelo.tipo import Tipo


def test_tipo_con_descripcion_puede_ser_creado():

    # dado
    tipo = Tipo('Electricidad')

    # cuando
    resultado = tipo.valor

    # entonces
    assert resultado == 'Electricidad'
