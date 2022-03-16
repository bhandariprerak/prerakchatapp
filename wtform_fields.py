from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User
#InputRequired will throw an error if user tries to submit the form with blank fields
#Length will allow us to set a minimum and maximum no. of characters required for the field.
#EqualTo compares the input of two different fields and throws an error if they aren't identical

#to define the form we need to give it a name
#Let's call it RegistrationForm
class RegistrationForm(FlaskForm):
    """Registration Form"""
    """it has 3 fields : username, password, and password confirmation"""
    #each of them will be declared as a class attribute

    #username will be of type String
    #the 'username_label' is label tag in html
    username = StringField('username_label', validators=[InputRequired(message="Username required"),
                            Length(min=3, max=25, message="Username must be between 3 and 25 characters")])
    password = PasswordField('password_label',validators=[InputRequired(message="Password required"),
                            Length(min=6, max=10, message="Password must be between 6 and 10 characters")])
    confirm_pswd = PasswordField('confirm_pswd_label',validators=[InputRequired(message="Password required"),
                            EqualTo('password', message="Passwords must match")])
    submit_button = SubmitField('Create')

    #creating custom validotors:
    #1) for username : to check for duplicates.
    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exists. Select a different username.")
