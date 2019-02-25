from modelo.concepto import Concepto


def test_concepto_con_descripcion_puede_ser_creado():

    # dado
    concepto = Concepto('Factura de agua')

    # cuando
    resultado = concepto.valor

    # entonces
    assert resultado == 'Factura de agua'
