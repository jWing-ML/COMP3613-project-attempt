from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_dist
)

dist_views = Blueprint('dist_views', __name__, template_folder='../templates')


@dist_views.route('/api/dist', methods=['POST'])
def create_dist_action():
    dist = create_dist()
    dist.distribute()
    return jsonify({"message":"done created"})
