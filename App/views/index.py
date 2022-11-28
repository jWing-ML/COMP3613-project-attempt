from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import User

from datetime import date

from flask_login import current_user
from App.controllers import (
    create_feed,
    get_all_feed,
    create_dist,
    get_all_users,
    create_user,
    get_dist_by_id
)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    
    create_user("bob", "password")
    create_user("betty", "password")

    

    return render_template('login.html')