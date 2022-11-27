from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
import datetime
from datetime import timedelta


from App.controllers import (
    create_dist,
    get_all_dist_json,
    update_dist
)

dist_views = Blueprint('dist_views', __name__, template_folder='../templates')


@dist_views.route('/api/dist', methods=['POST'])
def create_dist_action():
    dist = create_dist()
    dist.distribute()
    return jsonify({"message":"done created"})


# list dist
@dist_views.route('/dist/list', methods=['GET'])
def get_all_dist_action():
    dist = get_all_dist_json()
    return jsonify(dist)



@dist_views.route('/dist/update', methods=['PUT'])
def update_dist_action():
    data = request.json
    dist = update_dist(data['id'],  data['timeStamp'])   #int(data['timeStamp'])
    if dist:
        return jsonify({"message":"distribution Updated"})
    return jsonify({"message":"distribution Not Found"})