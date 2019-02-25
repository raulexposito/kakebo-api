import csv

from flask import Flask
from modelo.movimiento import Movimiento
from modelo.concepto import Concepto
from modelo.fecha import Fecha

app = Flask(__name__)


@app.route('/')
def index():

    miarray = []
    with open('file.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            miarray.append(
                Movimiento(
                    concepto=Concepto('el concepto'),
                    fecha=Fecha(),
                    cantidad='1000',
                    tipo='el tipo',
                    entidad='la entidad'))

    return miarray[0].como_json()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
