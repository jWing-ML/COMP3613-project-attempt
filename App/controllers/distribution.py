from App.models import Distribution
from App.database import db
from datetime import date

def create_dist(numprofiles):
    dist = Distribution(numprofiles)
    db.session.add(dist)
    db.session.commit()
    return dist

def distribute():
    users = User.query.all()
    numprofiles=len(users)
    for user in users:
         feed = create_feed()
    return dist

def get_dist_by_id(distID):
    return  Distribution.query.get(distID)

def get_last_distribution_JSON():
    d=Distribution.query.all() 
    num=0
    for i in d:
        num = num+1
    dist = Distribution.query.filter_by(id=num)
    if not dist:
        return []
    dist = [dis.toJSON() for dis in dist]
    return dist
    

