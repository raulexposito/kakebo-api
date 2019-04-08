from flask import Flask, jsonify
from modelo.movimientos import movimientos
from adaptadores.lectorCSV import lectorCSV

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

movimientos = movimientos(lectorCSV.leer_movimientos('datos/movimientos.csv'))


@app.route('/todos', methods=['GET'])
def todos():
    return como_json(movimientos.todos())


@app.route('/ultimo_mes', methods=['GET'])
def ultimo_mes():
    return como_json(movimientos.ultimos_meses(1))


@app.route('/ultimos_seis_meses', methods=['GET'])
def ultimos_seis_meses():
    return como_json(movimientos.ultimos_meses(6))


@app.route('/ultimo_ano', methods=['GET'])
def ultimo_ano():
    return como_json(movimientos.ultimos_meses(12))


def como_json(movimientos):
    return jsonify(movimientos.como_dict())


if __name__ == '__main__':
    app.run()
