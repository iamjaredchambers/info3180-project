from . import db

class PropertyProfile(db.Model):
       
       __tablename__ = 'property'
       id = db.Column(db.Integer, primary_key = True)
       propertyTitle = db.Column(db.String(255))
       propertyType = db.Column(db.String(255), nullable = False)
       description = db.Column(db.String(255))
       location = db.Column(db.String(255))
       numberofrooms = db.Column(db.Integer)
       numberofbathrooms = db.Column(db.Integer)
       price = db.Column(db.Integer)
       filename =  db.Column(db.String(80))
       
       def __init__(self, propertyTitle, propertyType, description, location, numberofrooms, numberofbathrooms, price, filename):
              self.propertyTitle = propertyTitle
              self.propertyType = propertyType
              self.description = description 
              self.location = location
              self.numberofrooms = numberofrooms
              self.numberofbathrooms = numberofbathrooms
              self.price = price
              self.filename = filename
       
       def __repr__(self):
        return '<Property %r>' % (self.propertyTitle)
       
       
       
       
       
       
    
