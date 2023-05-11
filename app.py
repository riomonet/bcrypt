from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Proclamations
from forms import Registration_Form, Login_Form, Proc_Form
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


@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = Registration_Form()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        firstname = (form.firstname.data).upper()
        lastname = (form.lastname.data).upper()
        new_user = User.register(username, password, email,firstname,lastname)
        # need error handling for duplicate user names
        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append("THERE CAN ONLY BE ONE")
            return render_template('register.html', form = form)

        session['username'] = new_user.username
        flash('Accepted into the secret society' ,'success')
        return redirect(f'/proclamations/{username}')
         
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        username = form.username.data
        pw = form.password.data
        user = User.authenticate(username, pw)
        if user:
            flash(f'we declare {user.username}, a valued member of our society','success')
            session['username'] = user.username
            return redirect(f'/proclamations/{user.username}')
        else:
            flash('fuck off', 'danger')
            form.username.errors = ['you are not welcome here']

    return render_template ('login.html', form = form)



@app.route('/proclamations/<username>', methods=['GET','POST'])
def show_procs(username):
    if username != session['username']:
        flash("NO TRESPASSING",'danger')
        return redirect('/')
    form = Proc_Form()
    u = User.query.get(username)
    all = Proclamations.query.all()
    if form.validate_on_submit():
        text = form.text.data
        title = form.title.data
        entry = Proclamations(title=title,text=text, username = username)
        db.session.add(entry)
        db.session.commit()
        return redirect(f'/proclamations/{username}')

    return render_template("proclamations.html", form = form, all = all,u = u)


@app.route('/logout')
def logout():
    session.pop('username')
    flash ('Sayounara Sucker!','primary')
    return redirect('/')



@app.route('/users/<username>/delete', methods=['POST'])
def delete(username):
    session.pop('username')
    flash ('Sayounara Sucker!','primary')
    user = User.query.get_or_404(username)
    for proc in user.proclamations:
        db.session.delete(proc)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')


@app.route('/proclamations/<int:id>/update', methods=['GET','POST'])
def update_proc(id):

    post = Proclamations.query.get_or_404(id)
    form = Proc_Form(obj=post)
    username=post.username
    if username != session['username']:
        flash("NO TRESPASSING",'danger')
        return redirect('/')
    
    if form.validate_on_submit():
        post.text = form.text.data
        post.title = form.title.data
        db.session.commit()
        return redirect(f'/proclamations/{username}')

    return render_template("edit.html", form = form, all = all)

@app.route('/proclamations/<int:id>/delete', methods=['POST'])
def delete_proc(id):

    post = Proclamations.query.get_or_404(id)
    username=post.username
    if username != session['username']:
        flash("NO TRESPASSING",'danger')
        return redirect('/')
    db.session.delete(post)
    db.session.commit()
    return redirect (f"/proclamations/{username}")





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






