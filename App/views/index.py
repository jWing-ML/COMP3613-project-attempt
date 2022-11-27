from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models import User

from flask_login import current_user
from App.controllers import (
    create_feed,
    get_all_feed,
    create_dist,
    get_all_users,
    create_user
)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():

    create_user("John", 'pass')
    create_user("Jane", 'pass')
    create_user("Mark", 'pass')

    users=User.query.all()
    numprofiles=len(users)
    dist = create_dist(numprofiles)
    
    for user in users:
        feed = create_feed( user.id , dist.id )
    
    feeds = get_all_feed()
    users= get_all_users()

    return render_template('feed.html', users= users, feeds=feeds)