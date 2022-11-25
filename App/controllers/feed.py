from App.models import Distribution
from App.database import db
from random import randint

def create_feed(receiverID, distID):

    dist = Distribution.query.get(distID)

    senderID = randint(0, dist)
    while (senderID == receiverID):                    #ensures the senderID is not the recieverID
        senderID = randint(0, dist.numprofiles)

    feed = Feed(senderID, receiverID, distID)
    db.session.add(feed)
    db.session.commit()
    return feed

def get_all_feed():
    feeds = Feed.query.all()
    if not feed:
        return []
    feed = [feed.toJSON() for feed in feeds]
    return feed

    

