
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired


"""Forms for playlist app."""

from wtforms import SelectField
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)






# class Registration_Form(FlaskForm):
#     """form for registering users"""

#     username  = StringField("Username",   validators=[InputRequired()])
#     password  = PasswordField("Password", validators=[InputRequired()])
#     email     = StringField("email address", validators=[InputRequired()])
#     firstname = StringField("First Name", validators=[InputRequired()])
#     lastname  = StringField("Last Name", validators=[InputRequired()])

# class Login_Form(FlaskForm):
#     """form for logging in"""
#     username  = StringField("Username",   validators=[InputRequired()])
#     password  = PasswordField("Password", validators=[InputRequired()])

    
# class Proc_Form(FlaskForm):
#     title = StringField("with Authority", validators=[InputRequired()])
#     text = StringField("State Your Case", validators=[InputRequired()])
    
