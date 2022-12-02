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
    get_dist_by_id,
    create_image
)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    
    create_user("bob", "password")
    create_image("1", "https://th.bing.com/th/id/OIP.-A2Z_EY0ick_wctAjgUqZQHaET?w=318&h=184&c=7&r=0&o=5&pid=1.7")

    create_user("betty", "password")
    create_image("2", "https://th.bing.com/th/id/OIP.9nzbJlzKhuMzTLUOpObDDQHaHC?w=204&h=194&c=7&r=0&o=5&pid=1.7")

    create_user("brian", "password")
    create_image("3", "https://i0.wp.com/www.urbandognyc.com/wp-content/uploads/2018/10/brian-family-guy-dog-brought-back-to-life.jpg?fit=1500%2C1500&ssl=1")
    
    create_user("becky", "password")
    create_image("4", "https://th.bing.com/th/id/OIP.of0QWVWaAAm1hZcefnxmhwAAAA?pid=ImgDet&rs=1")
    
    
   

    

    return render_template('login.html')