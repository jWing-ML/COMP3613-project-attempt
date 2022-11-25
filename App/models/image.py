from App.database import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120), nullable=False)
    userId =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)                               #owner of the image
    rankings = db.relationship('Ranking', backref='ranking', lazy=True, cascade="all, delete-orphan")       #other users rank of the image

    def __init__(self, userId, url):
        self.userId = userId
        self.url = url

    def toJSON(self):
        return{
            'id': self.id,
            'url': self.url,
            'userId': self.userId,
            'rankings': [ranking.toJSON() for ranking in self.rankings]
        }
