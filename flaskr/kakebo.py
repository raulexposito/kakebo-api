from flask import Flask, jsonify
from flask_cors import CORS
from modelo.movimientos import movimientos
from adaptadores.lectorCSV import lectorCSV

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/todos', methods=['GET'])
def todos():
    return como_json(leer_movimientos().todos())


@app.route('/ultimo_mes', methods=['GET'])
def ultimo_mes():
    return como_json(leer_movimientos().ultimos_meses(1))


@app.route('/ultimos_tres_meses', methods=['GET'])
def ultimos_tres_meses():
    return como_json(leer_movimientos().ultimos_meses(3))


@app.route('/ultimos_seis_meses', methods=['GET'])
def ultimos_seis_meses():
    return como_json(leer_movimientos().ultimos_meses(6))


@app.route('/ultimo_ano', methods=['GET'])
def ultimo_ano():
    return como_json(leer_movimientos().ultimos_meses(12))


def como_json(movimientos):
    return jsonify(movimientos.como_dict())


def leer_movimientos():
    return movimientos(lectorCSV.leer_movimientos('datos/movimientos.csv'))


if __name__ == '__main__':
    app.run()
