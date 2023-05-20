from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///auth_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "thesecretekey898912"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
with app.app_context():
    connect_db(app)

@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


# @app.route("/playlists/<int:playlist_id>")
# def show_playlist(playlist_id):
#     """Show detail on specific playlist."""
#     return redirect('/')
#     # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


# @app.route("/playlists/add", methods=["GET", "POST"])
# def add_playlist():
#     """Handle add-playlist form:

#     - if form not filled out or invalid: show form
#     - if valid: add playlist to SQLA and redirect to list-of-playlists
#     """

#     # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
#     return redirect('/')

# ##############################################################################
# # Song routes


# @app.route("/songs")
# def show_all_songs():
#     """Show list of songs."""

#     songs = Song.query.all()
#     return render_template("songs.html", songs=songs)


# @app.route("/songs/<int:song_id>")
# def show_song(song_id):
#     """return a specific song"""

#     # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


# @app.route("/songs/add", methods=["GET", "POST"])
# def add_song():
#     """Handle add-song form:

#     - if form not filled out or invalid: show form
#     - if valid: add playlist to SQLA and redirect to list-of-songs
#     """

#     # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


# @app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
# def add_song_to_playlist(playlist_id):
#     """Add a playlist and redirect to list."""

#     # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

#     # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

#     playlist = Playlist.query.get_or_404(playlist_id)
#     form = NewSongForPlaylistForm()

#     # Restrict form to songs not already on this playlist

#     curr_on_playlist = ...
#     form.song.choices = ...

#     if form.validate_on_submit():

#           # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

#           return redirect(f"/playlists/{playlist_id}")

#     return render_template("add_song_to_playlist.html",
#                              playlist=playlist,
#                              form=form)


















    
# @app.route('/')
# def home():
#     return render_template('index.html')
    
# @app.route('/register', methods=['GET', 'POST'])
# def register_user():
#     form = Registration_Form()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data
#         email = form.email.data
#         firstname = (form.firstname.data).upper()
#         lastname = (form.lastname.data).upper()
#         new_user = User.register(username, password, email,firstname,lastname)
#         # need error handling for duplicate user names
#         db.session.add(new_user)
#         try:
#             db.session.commit()
#         except IntegrityError:
#             form.username.errors.append("THERE CAN ONLY BE ONE")
#             return render_template('register.html', form = form)

#         session['username'] = new_user.username
#         flash('Accepted into the secret society' ,'success')
#         return redirect(f'/proclamations/{username}')
         
#     return render_template('register.html', form=form)


# @app.route('/login', methods=['GET','POST'])
# def login():
#     form = Login_Form()
#     if form.validate_on_submit():
#         username = form.username.data
#         pw = form.password.data
#         user = User.authenticate(username, pw)
#         if user:
#             flash(f'we declare {user.username}, a valued member of our society','success')
#             session['username'] = user.username
#             return redirect(f'/proclamations/{user.username}')
#         else:
#             flash('fuck off', 'danger')
#             form.username.errors = ['you are not welcome here']

#     return render_template ('login.html', form = form)



# @app.route('/proclamations/<username>', methods=['GET','POST'])
# def show_procs(username):
#     if username != session['username']:
#         flash("NO TRESPASSING",'danger')
#         return redirect('/')
#     form = Proc_Form()
#     u = User.query.get(username)
#     all = Proclamations.query.all()
#     if form.validate_on_submit():
#         text = form.text.data
#         title = form.title.data
#         entry = Proclamations(title=title,text=text, username = username)
#         db.session.add(entry)
#         db.session.commit()
#         return redirect(f'/proclamations/{username}')

#     return render_template("proclamations.html", form = form, all = all,u = u)


# @app.route('/logout')
# def logout():
#     session.pop('username')
#     flash ('Sayounara Sucker!','primary')
#     return redirect('/')



# @app.route('/users/<username>/delete', methods=['POST'])
# def delete(username):
#     session.pop('username')
#     flash ('Sayounara Sucker!','primary')
#     user = User.query.get_or_404(username)
#     for proc in user.proclamations:
#         db.session.delete(proc)
#     db.session.delete(user)
#     db.session.commit()
#     return redirect('/')


# @app.route('/proclamations/<int:id>/update', methods=['GET','POST'])
# def update_proc(id):

#     post = Proclamations.query.get_or_404(id)
#     form = Proc_Form(obj=post)
#     username=post.username
#     if username != session['username']:
#         flash("NO TRESPASSING",'danger')
#         return redirect('/')
    
#     if form.validate_on_submit():
#         post.text = form.text.data
#         post.title = form.title.data
#         db.session.commit()
#         return redirect(f'/proclamations/{username}')

#     return render_template("edit.html", form = form, all = all)

# @app.route('/proclamations/<int:id>/delete', methods=['POST'])
# def delete_proc(id):

#     post = Proclamations.query.get_or_404(id)
#     username=post.username
#     if username != session['username']:
#         flash("NO TRESPASSING",'danger')
#         return redirect('/')
#     db.session.delete(post)
#     db.session.commit()
#     return redirect (f"/proclamations/{username}")


 


# create a create read update delete flask templating system in emacs.
# call prot
    

# # salt = bcrypt.gensalt()(rounds=14) can specify the number of rounds of hash
# b'$2b$12$LCPOoA1emZ7s.rXseGE15.tDVAsJz69fb6FdFaU.6nyZxRthUN59u'
#  $2b = bcrypt identifier
#  $12 = 12 rounds of hash the hight number the more secure
# i dont understand workfactor and the salt


# salt = bcrypt.gensalt()

# print(salt)
# password = b'arile'
# bcrypt.hashpw(b'password',salt)

# bcrypt = Bcrypt()


# pw = 'thefunnythingis'

# hashed_pw = bcrypt.generate_password_hash(pw)

# bcrypt.check_password_hash(hashed_pw, pw)






