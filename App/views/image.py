from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import current_user

from App.controllers import (
    create_image, 
    get_all_images,
    get_all_images_json,
    get_images_by_userid_json,
    get_image,
    get_image_json,
    delete_image,
    get_user
)

image_views = Blueprint('image_views', __name__, template_folder='../templates')

#working
#user can post the same pic as many times as they want

@image_views.route('/newimage', methods=['POST'])
def create_image_action():

    url = request.form.get('url')

    user = current_user
    image = create_image(current_user.id, url)
    return  render_template('profile.html',user=user)



@image_views.route('/api/images/user/<userId>', methods=['GET'])
def get_images_by_user_action(userId):
    images = get_images_by_userid_json(userId)
    return jsonify(images)






@image_views.route('/images', methods=['GET'])
def get_image_page():
    images = get_all_images()
    return render_template('images.html', images=images)

@image_views.route('/api/images', methods=['GET'])
def get_images_all_action():
    images = get_all_images_json()
    return jsonify(images)



@image_views.route('/api/images/id', methods=['GET'])
def get_images_by_id_action():
    data = request.json
    image = get_image_json(data['id'])
    return jsonify(image)

@image_views.route('/api/images', methods=['DELETE'])
def delete_image_action():
    data = request.json
    if get_image(data['id']):
        delete_image(data['id'])
        return jsonify({"message":"Image Deleted"}) 
    return jsonify({"message":"Image Not Found"}) 