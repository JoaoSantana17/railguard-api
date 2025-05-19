from flask import Blueprint, request, jsonify

login_bp = Blueprint('login', __name__)

login_data = [
    {"id": 1, "username": "admin", "senha": "1234"},
    {"id": 2, "username": "joao", "senha": "joao1234"},
    {"id": 3, "username": "jun", "senha": "jun1234"},
    {"id": 4, "username": "yuri", "senha": "yuri1234"},
]

@login_bp.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = [{'id': u['id'], 'username': u['username']} for u in login_data]
    return jsonify(usuarios), 200

@login_bp.route('/', methods=['POST', 'OPTIONS'])
def fazer_login():
    if request.method == 'OPTIONS':
        return '', 200

    dados = request.get_json()
    username = dados.get('username')
    senha = dados.get('senha')

    for user in login_data:
        if user['username'] == username and user['senha'] == senha:
            return jsonify({'msg': 'Login bem-sucedido!'}), 200
    return jsonify({'msg': 'Usuário ou senha inválidos.'}), 401
