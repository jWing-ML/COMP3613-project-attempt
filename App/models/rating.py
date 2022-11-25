from App.database import db

#Ratings are created by users when they rate other users' profiles
class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creatorId =  db.Column(db.Integer,  nullable=False)         #self 
    targetId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)          #the profile id being rated
    score = db.Column(db.Integer, nullable=False)                                       #the rating (1-5)                             
    
    def __init__(self, creatorId, targetId, score):
        self.creatorId = creatorId
        self.targetId = targetId
        self.score = score
    
    def toJSON(self):
        return{
            'id': self.id,
            'creatorId': self.creatorId,
            'targetId': self.targetId,
            'score': self.score,
            'timeStamp': self.timeStamp
        }
