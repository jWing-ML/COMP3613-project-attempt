from App.database import db
import datetime 

class Distribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numprofiles = db.Column(db.Integer, nullable=False)    
    timeStamp = db.Column(db.DateTime , nullable=False)                         
                  

    def __init__(self, numprofiles):
        self.numprofiles = numprofiles
        self.timeStamp = datetime.datetime.now() 


    def toJSON(self):
        return{
            'id': self.id,
            'numprofiles': self.numprofiles,
            'timestamp': self.timeStamp
        }