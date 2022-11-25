from App.models import Distribution
from App.database import db

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
    distr = Distribution.query.filter_by(id=distID)
    if not distr:
        return []
    dist = [dist.toJSON() for dist in distr]
    return dist

def get_last_distribution():
    dist = Distribution.query.all()
    if not dist:return []
    size=len(dist)
    dist = Distribution.query.filter_by(id = size)
    return dist
    

