from modelo.entidad import Entidad


def test_entidad_con_descripcion_puede_ser_creada():

    # dado
    entidad = Entidad('Hacienda')

    # cuando
    resultado = entidad.valor

    # entonces
    assert resultado == 'Hacienda'
