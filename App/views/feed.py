from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from datetime import date
from flask_login import current_user

from App.models import User, Distribution

from App.controllers import (
    create_feed,
    get_all_feed,
    create_dist,
    get_last_distribution_JSON,
    get_feed_by_receiverID,
    get_user
)

feed_views = Blueprint('feed_views', __name__, template_folder='../templates')


@feed_views.route('/api/feed', methods=['GET'])
def create_feed_action():

    users=User.query.all()
    numprofiles=len(users)
    dist = create_dist(numprofiles)
    flash(dist.timeStamp)
    for user in users:
        feed = create_feed( user.id , dist.id )
    
    
    return jsonify({"message":"distributed"})



#for UI
@feed_views.route('/api/feeds', methods=['GET'])
def view_all_feed():
    
    feeds = get_feed_by_receiverID(current_user.id)
    users = [get_user(feed.senderID) for feed in feeds]

    return render_template('feed.html', users=users, feeds= feeds)

#for UI
@feed_views.route('/api/profile', methods=['GET'])
def view_profile():
    return render_template('profile.html',user=current_user)
