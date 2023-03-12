from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed, FileField

class PropertyForm(FlaskForm):
    propertyTitle = StringField('Property Title', validators = [InputRequired()])
    description = StringField('Description', validators = [InputRequired()])
    numberofrooms = StringField('Number of Rooms', validators = [InputRequired()])
    numberofbathrooms = StringField('Number of Bathrooms', validators = [InputRequired()])
    price = StringField('Price', validators = [InputRequired()])
    propertytype = StringField('Property Type')
    location = StringField('Property Location', validators = [InputRequired()])
    photo = FileField('Choose a file', validators = [FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only!')])
    
