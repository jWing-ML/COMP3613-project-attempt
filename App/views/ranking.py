from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash
from flask_jwt import jwt_required
from flask_login import current_user


from App.controllers import (
    create_ranking, 
    get_all_rankings,
    get_all_rankings_json,
    get_ranking,
    get_rankings_by_image,
    get_rankings_by_creator,
    get_ranking_by_actors,
    get_calculated_ranking,
    update_ranking,
    #delete_ranking,
    get_user,
    get_image,
    get_user,
    get_feed_by_receiverID
)

ranking_views = Blueprint('ranking_views', __name__, template_folder='../templates')


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

@ranking_views.route('/create/rank/<score>/<imgID>/<creator>', methods=['GET'])
def create_ranking_action_ui(score, imgID, creator):

    img= get_image(imgID)
    if get_user(creator) and img:

        lock = get_ranking_by_actors(creator, img.id)           #check if the user already rank the img
        if lock:
            flash("user already rank image")
        else:
            ranking = create_ranking(creator, img.id, score)
            flash("created sucessfully")

        user=get_user(img.userId)

        return render_template('profile.html', user=user)

    return flash("user not found")


@ranking_views.route('/view/rankings', methods=['GET'])
def get_all_rankings_action_ui():
    rankings = get_rankings_by_creator(current_user.id)
    if rankings:
        return render_template('rankings.html', rankings=rankings)
    else:
        flash("You have not ranked any images")
        return render_template('profile.html', user=current_user)


@ranking_views.route('/api/rankings', methods=['GET'])
def get_all_rankings_action():
    rankings = get_all_rankings_json()
    return jsonify(rankings)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

@ranking_views.route('/api/rankings', methods=['POST'])
def create_ranking_action():
    data = request.json
    if get_user(data['creatorId']) and get_image(data['imageId']):
        image = get_image(data['imageId'])
        if data['creatorId'] != image.userId:

            prev = get_ranking_by_actors(data['creatorId'], data['imageId'])
            if prev:
                return jsonify({"message":"Current user already ranked this image"}) 
            ranking = create_ranking(data['creatorId'], data['imageId'], data['score'])
            return jsonify({"message":"Ranking created"}) 

        return jsonify({"message":"User cannot rank self"})
    return jsonify({"message":"User not found"}) 



@ranking_views.route('/api/rankings/<imgId>', methods=['GET'])
def get_rankings_by_image_action(imgId):
    data = request.json
    if get_image(imgId):
        ranking = get_rankings_by_image(imgId)
        if ranking:
            return jsonify(ranking)
    return jsonify({"message":"Image Not Found"})



@ranking_views.route('/api/rankings/byid', methods=['GET'])
def get_ranking_action():
    data = request.json
    ranking = get_ranking(data['id'])
    if ranking:
        return ranking.toJSON()
    return jsonify({"message":"Ranking Not Found"})

@ranking_views.route('/api/rankings/bycreator', methods=['GET'])
def get_rankings_by_creator_action():
    data = request.json
    if get_user(data['creatorId']):
        ranking = get_rankings_by_creator(data['creatorId'])
        if ranking:
            return jsonify(ranking)
    return jsonify({"message":"User Not Found"})



@ranking_views.route('/api/rankings', methods=['PUT'])
def update_ranking_action():
    data = request.json
    ranking = update_ranking(data['id'], data['score'])
    if ranking:
        return jsonify({"message":"Ranking updated"})
    return jsonify({"message":"Ranking not found"})

# @ranking_views.route('/api/rankings', methods=['DELETE'])
# def delete_ranking_action():
#     data = request.json
#     if get_ranking(data['id']):
#         delete_ranking(data['id'])
#         return jsonify({"message":"Ranking deleted"}) 
#     return jsonify({"message":"Ranking not found"}) 

@ranking_views.route('/api/rankings/calc', methods=['GET'])
def get_calculated_ranking_action():
    data = request.json
    if get_image(data['imageId']):
        ranking = get_calculated_ranking(data['imageId'])
        if ranking:
            return jsonify({"calculated_ranking": ranking}) 
        return jsonify({"message":"No rankings by this image found"})
    return jsonify({"message":"Image not found"})
