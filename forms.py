
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class Registration_Form(FlaskForm):
    """form for registering users"""

    username  = StringField("Username",   validators=[InputRequired()])
    password  = PasswordField("Password", validators=[InputRequired()])
    email     = StringField("email address", validators=[InputRequired()])
    firstname = StringField("First Name", validators=[InputRequired()])
    lastname  = StringField("Last Name", validators=[InputRequired()])

class Login_Form(FlaskForm):
    """form for logging in"""
    username  = StringField("Username",   validators=[InputRequired()])
    password  = PasswordField("Password", validators=[InputRequired()])

    
class Proc_Form(FlaskForm):
    title = StringField("with Authority", validators=[InputRequired()])
    text = StringField("State Your Case", validators=[InputRequired()])
    
