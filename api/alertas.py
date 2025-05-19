from flask import Blueprint, request, jsonify

alertas_bp = Blueprint('alertas', __name__)

alertas_data = [
    {'id': 1, 'Linha': '8-Diamante', 'vagao': '2', 'atividade': 'Vendedor Ambulante/Movimentação Suspeita', 'status': 'ativo'},
    {'id': 2, 'Linha': '9-Esmeralda', 'vagao': '7', 'atividade': 'Movimentação Suspeita', 'status': 'ativo'},
]

@alertas_bp.route('/', methods=['GET'])
def listar_alertas():
    return jsonify(alertas_data), 200

@alertas_bp.route('/', methods=['POST', 'OPTIONS'])
def adicionar_alerta():
    if request.method == 'OPTIONS':
        return '', 200

    novo_alerta = request.get_json()
    if not novo_alerta.get('Linha') or not novo_alerta.get('vagao') or not novo_alerta.get('atividade'):
        return jsonify({'msg': 'Campos Linha, vagao e atividade são obrigatórios.'}), 400

    novo_alerta['id'] = max(a['id'] for a in alertas_data) + 1 if alertas_data else 1
    novo_alerta['status'] = 'ativo'
    alertas_data.append(novo_alerta)
    return jsonify({'msg': 'Alerta adicionado com sucesso'}), 201

@alertas_bp.route('/<int:id>', methods=['PUT', 'OPTIONS'])
def atualizar_alerta(id):
    if request.method == 'OPTIONS':
        return '', 200

    dados = request.get_json()
    novo_status = dados.get('status')
    if novo_status not in ['ativo', 'resolvido', 'ignorado']:
        return jsonify({'msg': "Status inválido. Use 'ativo', 'resolvido' ou 'ignorado'."}), 400

    for alerta in alertas_data:
        if alerta['id'] == id:
            alerta['status'] = novo_status
            return jsonify({'msg': 'Status do alerta atualizado com sucesso'}), 200

    return jsonify({'msg': 'Alerta não encontrado'}), 404

@alertas_bp.route('/<int:id>', methods=['DELETE', 'OPTIONS'])
def deletar_alerta(id):
    if request.method == 'OPTIONS':
        return '', 200

    for alerta in alertas_data:
        if alerta['id'] == id:
            alertas_data.remove(alerta)
            return jsonify({'msg': 'Alerta excluído com sucesso'}), 200

    return jsonify({'msg': 'Alerta não encontrado'}), 404
