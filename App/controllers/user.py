from App.models import User, Rating
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    if user:
        user = user.toJSON()
    return user

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toJSON() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        db.session.commit()
        return user
    return None

def delete_user(id):
    user = get_user(id)
    if user:
        db.session.delete(user)
        return db.session.commit()
    return None

def get_ratings_by_target(targetId):
    ratings = Rating.query.filter_by(targetId=targetId)

    return ratings

def get_top_profiles():

    firstTotal = 0
    secondTotal = 0
    thirdTotal = 0 

    firstUser = None
    secondUser = None
    thirdUser = None

    

    users = get_all_users()
    for user in users:
        num5stars = 0
        num4stars = 0
        num3stars = 0
        num2stars = 0
        num1stars = 0
        ratings = get_ratings_by_target(user.id)
        if ratings:
            for rating in ratings:
                if rating.score == 5:
                    num5stars = num5stars + 1
                if rating.score == 4:
                    num4stars = num4stars + 1
                if rating.score == 3:
                    num3stars = num3stars + 1
                if rating.score == 2:
                    num2stars = num2stars + 1
                if rating.score == 1:
                    num1stars = num1stars + 1

            total = str(num5stars) + str(num4stars) + str(num3stars) + str(num2stars) + str(num1stars)

            if int(total) > firstTotal:
                thirdUser = secondUser
                secondUser = firstUser
                firstUser = user 
                thirdTotal = secondTotal
                secondTotal = firstTotal
                firstTotal = int(total)
            else:
                if int(total) < firstTotal and int(total) > secondTotal :
                    thirdUser = secondUser
                    secondUser = user
                    thirdTotal = secondTotal
                    secondTotal = int(total)
                else:
                    if int(total) < secondTotal and int(total) > thirdTotal:
                        thirdUser = user
                        thirdTotal = int(total)

    users = [firstUser, secondUser, thirdUser]
    return users
