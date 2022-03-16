from flask import Flask, render_template
from wtform_fields import *
from models import *
# from flask_sqlalchemy import SQLAlchemy
#render_template is used to return html file in index() function
#give name to flask for central callable object
"""configure app"""
app = Flask( __name__ )

#this secret key will be used by flask to sign the cookies used during the session.
# it keeps client side secure
# it is a passphrase known only to us
app.secret_key = 'replace later'

#configure database to tell flask-alchemy the location of database we will be accessing
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://fhqsvjylatmbet:5d1d77f4288448e83cb671738a4f670e3ca54399ad988debfba70e1c71839b84@ec2-44-193-188-118.compute-1.amazonaws.com:5432/db7lurilbejqnr"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#initialize the connection to our database
db = SQLAlchemy(app)

#for every page of website we will define a function.
#this function will say what actions we want python to take and which content to display
# this is done using decorators
#the "/" shows the page at which we want this to apply to
#methods shows in which ways the user can access the page
@app.route("/", methods=['GET', 'POST'])
#this function will be triggered each time a user visits this page

def index():
    #here we instanciate the form
    reg_form = RegistrationForm()

    #we need to call validate after submit is clicked and that can be done using this function
    #if the submit gets any error, the function will return false.
    if reg_form.validate_on_submit() :
        #here after validation, we extract the username and password to store in our database
        username = reg_form.username.data
        password = reg_form.password.data

        #now we add the username and password to our database
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB!"

    #if we also need flask to display the registration form, we need to pass it in 2nd parameter as shown
    #we also need to add the form to index file
    return render_template("index.html", form = reg_form)

if __name__ == "__main__":

    app.run(debug=True)
