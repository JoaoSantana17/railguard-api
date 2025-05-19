from flask import Flask
from flask_cors import CORS
from api.login import login_bp
from api.alertas import alertas_bp
from api.monitoramento import monitoramento_bp

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "https://api-railguard.vercel.app"])

@app.route('/')
def home():
    return "RailGuard API - Use as rotas /login, /alertas ou /monitoramento"

app.register_blueprint(login_bp, url_prefix='/login', strict_slashes=False)
app.register_blueprint(alertas_bp, url_prefix='/alertas', strict_slashes=False)
app.register_blueprint(monitoramento_bp, url_prefix='/monitoramento', strict_slashes=False)

if __name__ == '__main__':
    app.run(debug=True)
