from App.database import db

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    senderID = db.Column(db.Integer, nullable=False)                                        #1 person in your feed
    receiverID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)                                      # owner of the feed    
    distID =  db.Column(db.Integer, db.ForeignKey('distribution.id'), nullable=False)        #which distribution it belongs to

    def __init__(self, senderID, receiverID, distID):
        self.senderID = senderID
        self.receiverID = receiverID
        self.distID = distID

    def toJSON(self):
        return{
            'id': self.id,
            'senderID': self.senderID,
            'receiverID': self.receiverID,
            'distID': self.distID
        }