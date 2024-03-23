from flask import Blueprint, jsonify, request
from models import Post, Template
from research_and_writer_crew import ResearchAndWriterCrew

post_bp = Blueprint('post', __name__)

@post_bp.route('/api/post/save', methods=['POST'])
def save_post():
  data = request.get_json()

  theme_to_search = data.get('theme')

  if len(theme_to_search) == 0:
    return jsonify({"error": "The theme should have more context"}), 400
  
  user_id = data.get('user_id')

  templates = Template.get_template_by_user_id(user_id = user_id)

  user_writing_format = [template["content"] for template in templates]

  user_writing_format = ' '.join(user_writing_format)
  
  crew = ResearchAndWriterCrew(user_writing_format, theme_to_search);

  content = crew.run()
  
  new_post = Post(
    theme = theme_to_search,
    content = content,
    user_id = user_id,
  )

  new_post.save()
  
  return jsonify({"message": "Post created with success", "content": content}), 201

@post_bp.route('/api/post/list', methods=['POST'])
def list_posts():
  data = request.get_json()

  user_id = data.get('user_id')

  if user_id is None:
    return jsonify({"error": "User id is required"}), 400
  
  posts = Post.get_posts_by_user_id(user_id = user_id)

  return jsonify({"posts": posts}), 200

  
  


