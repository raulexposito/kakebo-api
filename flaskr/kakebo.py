import csv

from flask import Flask
from modelo.movimiento import Movimiento
from modelo.concepto import Concepto
from modelo.fecha import Fecha
from modelo.cantidad import Cantidad

KAKEBO = Flask(__name__)


@KAKEBO.route('/')
def index():

    miarray = []
    with open('file.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            miarray.append(
                Movimiento(
                    concepto=Concepto('el concepto'),
                    fecha=Fecha(),
                    cantidad=Cantidad(123.45),
                    tipo='el tipo',
                    entidad='la entidad'))

    return miarray[0].como_json()


if __name__ == '__main__':
    KAKEBO.run(host='0.0.0.0')
