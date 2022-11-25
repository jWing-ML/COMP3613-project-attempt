from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models import User

from flask_login import current_user
from App.controllers import (
    create_feed,
    get_all_feed,
    create_dist,
    get_all_users
)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():

    users=User.query.all()
    numprofiles=len(users)
    dist = create_dist(numprofiles)
    
    for user in users:
        feed = create_feed( user.id , dist.id )
    
    feeds = get_all_feed()
    users= get_all_users()

    return render_template('feed.html', users= users, feeds=feeds)