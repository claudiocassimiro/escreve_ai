from flask import Blueprint

# Criando um blueprint para rotas relacionadas aos usuários
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Importe as rotas específicas para registrar no blueprint
from . import auth

# Registrar as rotas do blueprint
auth_bp.register_blueprint(auth.auth_bp)