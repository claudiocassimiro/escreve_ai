from flask import Blueprint

# Criando um blueprint para rotas relacionadas aos usuários
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Criando um blueprint para rotas relacionadas aos templates do usuários
template_bp = Blueprint('template', __name__, url_prefix='/template')

# Criando um blueprint para rotas relacionadas aos posts do usuários
post_bp = Blueprint('post', __name__, url_prefix='/post')

# Importe as rotas específicas para registrar no blueprint
from . import auth, template, post

# Registrar as rotas do blueprint
auth_bp.register_blueprint(auth.auth_bp)
template_bp.register_blueprint(template.template_bp)
post_bp.register_blueprint(post.post_bp)