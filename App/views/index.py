from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import User

from datetime import date

from flask_login import current_user
from App.controllers import (
    create_feed,
    get_all_feed,
    create_dist,
    get_all_users,
    get_last_distribution_JSON,
    create_user,
    get_dist_by_id
)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    
    create_user("bob", "password")
    create_user("betty", "password")

    users=User.query.all()
    numprofiles=len(users)
    distr = create_dist(numprofiles)

    if(distr.id==1):
        for user in users:
            feed = create_feed( user.id , distr.id )
    
        feeds = get_all_feed()
        users= get_all_users()
    else:

        dist = get_dist_by_id(distr.id-1)
        
        if(dist.timeStamp!=date.today()):

            for user in users:
                feed = create_feed( user.id , distr.id )
    
    feeds = get_all_feed()
    users= get_all_users()

    return render_template('feed.html', users= users, feeds=feeds)