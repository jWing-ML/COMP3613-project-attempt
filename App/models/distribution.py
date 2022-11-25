from App.database import db
from datetime import date

class Distribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numprofiles = db.Column(db.Integer, nullable=False)    
    timeStamp = db.Column(db.Date , nullable=False)                         
                  

    def __init__(self, numprofiles):
        self.numprofiles = numprofiles
        self.timeStamp = date.today()


    def toJSON(self):
        return{
            'id': self.id,
            'numprofiles': self.numprofiles,
            'timestamp': self.timeStamp
        }