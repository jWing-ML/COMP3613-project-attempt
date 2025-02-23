from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash
from flask_jwt import jwt_required


from App.controllers import (
    create_rating, 
    get_all_ratings,
    get_all_ratings_json,
    get_rating,
    get_ratings_by_target,
    get_ratings_by_creator,
    get_rating_by_actors,
    update_rating,
    get_user,
    get_calculated_rating,
    get_last_distribution,
    get_feed_by_distID
)

rating_views = Blueprint('rating_views', __name__, template_folder='../templates')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


@rating_views.route('/create/rating/<creatorID>/<targetID>/<score>', methods=['GET'])
def create_rating_action_ui(creatorID, targetID, score):

    creator = get_user(creatorID)
    target = get_user(targetID)

    if creator != target:           #if creator not rating own profile
        prev_rating = get_rating_by_actors(creator.id, target.id)
        if prev_rating:     #if creator already rated that profile
            flash("User already rated the profile.")
        else:
            new_rating = create_rating(creator.id, target.id, score)
            flash("profile rating created.")
    else:
        flash("cannot rate your own profile")
    #load page
    dist = get_last_distribution()
    feed = get_feed_by_distID(dist.id)
    user=get_user(targetID)
    return render_template('feed.html', user=user, feeds= feed)
    



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

@rating_views.route('/api/ratings', methods=['POST'])
def create_rating_action():

    data = request.json
    if get_user(data['creatorId']) and get_user(data['targetId']):
        if data['creatorId'] != data['targetId']:
            
            prev = get_rating_by_actors(data['creatorId'], data['targetId'])
            if prev:
                return jsonify({"message":"Current user already rated this user"}) 
            rating = create_rating(data['creatorId'], data['targetId'], data['score'])
            return jsonify({"message":"Rating created"}) 

        return jsonify({"message":"User cannot rate self"})
    return jsonify({"message":"User not found"}) 

@rating_views.route('/api/ratings', methods=['GET'])
def get_all_ratings_action():
    ratings = get_all_ratings_json()
    return jsonify(ratings)

@rating_views.route('/api/ratings/byid', methods=['GET'])
def get_rating_action():
    data = request.json
    rating = get_rating(data['id'])
    if rating:
        return rating.toJSON()
    return jsonify({"message":"Rating not found"})

@rating_views.route('/api/ratings/bycreator', methods=['GET'])
def get_rating_by_creator_action():
    data = request.json
    if get_user(data['creatorId']):
        rating = get_ratings_by_creator(data['creatorId'])
        if rating:
            return jsonify(rating) 
        return jsonify({"message":"No ratings by this user found"})
    return jsonify({"message":"User not found"})

@rating_views.route('/api/ratings/bytarget', methods=['GET'])
def get_rating_by_target_action():
    data = request.json
    if get_user(data['targetId']):
        rating = get_ratings_by_target(data['targetId'])
        if rating:
            return jsonify(rating) 
        return jsonify({"message":"No ratings for this user found"})
    return jsonify({"message":"User not found"})

@rating_views.route('/api/ratings', methods=['PUT'])
def update_rating_action():
    data = request.json
    rating = update_rating(data['id'], data['score'])
    if rating:
        return jsonify({"message":"Rating updated"})
    return jsonify({"message":"Rating not found"})

# @rating_views.route('/api/ratings', methods=['DELETE'])
# def delete_rating_action():
#     data = request.json
#     if get_rating(data['id']):
#         delete_rating(data['id'])
#         return jsonify({"message":"Rating deleted"}) 
#     return jsonify({"message":"Rating not found"}) 

@rating_views.route('/api/ratings/calc', methods=['GET'])
def get_calculated_rating_action():
    data = request.json
    if get_user(data['targetId']):
        rating = get_calculated_rating(data['targetId'])
        if rating:
            return jsonify({"calculated rating": rating}) 
        return jsonify({"message":"No ratings by this user found"})
    return jsonify({"message":"User not found"})

