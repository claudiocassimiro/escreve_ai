from flask import Blueprint, jsonify, request
from models import Template

template_bp = Blueprint('template', __name__)

@template_bp.route('/api/template/save', methods=['POST'])
def save_tamplate():
  data = request.get_json()

  content = data.get('content')

  if len(content) == 0:
    return jsonify({"error": "The template should have more context"}), 400
  
  new_template = Template(
    content = content,
    user_id = data.get('user_id'),
  )

  new_template.save()
  
  return jsonify({"message": "Template saved with success"}), 201

@template_bp.route('/api/template/list', methods=['POST'])
def list_templates():
  data = request.get_json()

  user_id = data.get('user_id')

  if user_id is None:
    return jsonify({"error": "User id is required"}), 400
  
  templates = Template.get_template_by_user_id(user_id = user_id)

  return jsonify({"templates": templates}), 200

  
  


