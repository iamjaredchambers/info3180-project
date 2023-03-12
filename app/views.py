"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from app.forms import PropertyForm
from app.models import PropertyProfile
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Properties to Enlist")

@app.route('/properties/create', methods = ['POST', 'GET'])
def properties():
    
   form = PropertyForm()
    
   if request.method == "POST":
       if form.validate_on_submit():
        propertyTitle = request.form['propertyTitle']
        description = request.form['description']
        numberofrooms = request.form['numberofrooms']
        numberofbathrooms = request.form['numberofbathrooms']
        price = request.form['price']
        propertytype = request.form['propertytype']
        location = request.form['location']
        photo = request.files['photo']
        
            
            #propertytype = request.args.get('propertyType', default=None)
        
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        
        entry =  PropertyProfile(propertyTitle, propertytype, description, location, numberofrooms, numberofbathrooms,  price, filename)
        
        flash('File Uploaded', 'success')
        db.session.add(entry)
        db.session.commit()
        
        return redirect(url_for('property')) 
    
         
   return render_template('newproperty.html' , form = form)
    
@app.route('/properties')
def property():
    properties  = db.session.execute(db.select(PropertyProfile)).scalars()
    return render_template("properties.html", properties = properties)

def get_images():
    rootdir = os.getcwd()
    #print (rootdir)
    filelist = []
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            filelist.append(file)
        return filelist

@app.route('/properties/<property_id>')

def view_properties(property_id):
    property_id = int(property_id)
    prop = db.session.execute(db.select(PropertyProfile).filter_by(id=property_id)).scalar_one()
    return render_template('propertyview.html', property = prop)

@app.route('/upload/<filename>')
def get_uploaded_images(filename):
    rootdir = os.getcwd()
    return send_from_directory(os.path.join(rootdir,app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

