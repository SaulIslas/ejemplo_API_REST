from base_simulada import challengers
import re
from flask import Flask, json, jsonify

app = Flask(__name__)


@app.route('/jugadores', methods=['GET'])
def get_jugadores():
    return jsonify(challengers)


@app.route('/jugadores/<string:req_position>', methods=['GET'])
def get_ByPosition(req_position):
    for jugador in challengers:
        if jugador['Position'] == req_position:
            return jsonify(jugador)
    return jsonify({"mensaje": "Jugador no encontrado"})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
