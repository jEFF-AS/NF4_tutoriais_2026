from flask import jsonify

from services.ipea_service import buscar_serie

def serie(codigo):

    dados = buscar_serie(codigo)

    return jsonify(dados)
