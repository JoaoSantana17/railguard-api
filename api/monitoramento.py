from flask import Blueprint, jsonify

monitoramento_bp = Blueprint('monitoramento', __name__)

monitoramento_data = [
    {
        "linha": "8-Diamante",
        "vagoes": [
            {"vagao": 1, "status": "normal", "ultima_atualizacao": "2025-05-19T10:00:00"},
            {"vagao": 2, "status": "alerta", "ultima_atualizacao": "2025-05-19T10:05:00"},
            {"vagao": 3, "status": "normal", "ultima_atualizacao": "2025-05-19T10:00:00"},
        ]
    },
    {
        "linha": "9-Esmeralda",
        "vagoes": [
            {"vagao": 1, "status": "normal", "ultima_atualizacao": "2025-05-19T10:02:00"},
            {"vagao": 2, "status": "normal", "ultima_atualizacao": "2025-05-19T10:03:00"},
            {"vagao": 7, "status": "alerta", "ultima_atualizacao": "2025-05-19T10:04:00"},
        ]
    }
]

@monitoramento_bp.route('/', methods=['GET'])
def listar_monitoramento():
    return jsonify(monitoramento_data), 200

@monitoramento_bp.route('/<linha>', methods=['GET'])
def monitorar_linha(linha):
    linha_normalizada = linha.lower()
    for item in monitoramento_data:
        if item['linha'].lower() == linha_normalizada:
            return jsonify(item), 200
    return jsonify({'msg': 'Linha não encontrada'}), 404
