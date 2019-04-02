from flask import Flask, jsonify
from modelo.movimientos import Movimientos

app = Flask(__name__)


@app.route('/')
def index():
    movimientos = Movimientos('datos/movimientos.csv')
    return jsonify(movimientos.como_dict())


if __name__ == '__main__':
    app.run()
