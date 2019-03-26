import csv

from flask import Flask
from flask_marshmallow import Marshmallow
from modelo.movimiento import Movimiento

app = Flask(__name__)
ma = Marshmallow(app)


@app.route('/')
def index():

    miarray = []
    with open('datos/movimientos.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            miarray.append(Movimiento(row))

    return movimientos_schema.jsonify(miarray)


if __name__ == '__main__':
    app.run()


class MovimientoSchema(ma.Schema):
    class Meta:
        fields = ('concepto', 'fecha', 'cantidad', 'tipo', 'entidad')


movimientos_schema = MovimientoSchema(many=True)
