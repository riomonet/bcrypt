f"""Models for Login App."""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
        db.init_app(app)

class User(db.Model):
        """site user"""

        __tablename__ = "users"

        username = db.Column(db.String(20), primary_key=True)

        password = db.Column(db.Text, nullable = False)


        email =   db.Column(db.String(50),
                            nullable = False,
                            unique = True)

        firstname = db.Column(db.String(30), nullable = False)

        lastname =  db.Column(db.String(30), nullable = False)

        @classmethod            # use class methods when you generate a new instance?

        def register(cls, username, pwd,email,first,last):
                """Register users with hashed password and retuer user"""
                hashed = bcrypt.generate_password_hash(pwd)
                # turn bytestring into normal (unicode utf8) string
                hashed_utf8 = hashed.decode("utf8")

                return cls(username=username,
                           password = hashed_utf8,
                           email = email,
                           firstname = first,
                           lastname=last)


        @classmethod
        def authenticate(cls, username, pwd):
                """validate user exists and password is correct
                return user if true else false"""

                u = User.query.filter_by(username=username).first()

                if u and bcrypt.check_password_hash(u.password, pwd):

                        return u

                else:
                        return False

        # i = db.relationship('Proclamation',
        #                                 backref='users',
        #                                 cascade="all, delete",
        #                                 passive_deletes=True)


                

class Proclamations(db.Model):
        """shout it out load!"""

        __tablename__ = "i_declare"

        id = db.Column(db.Integer, primary_key=True, autoincrement=True)

        title = db.Column(db.String(100),nullable = False)

        text = db.Column(db.Text, nullable = False)

        username = db.Column(db.String(20), db.ForeignKey('users.username', ondelete="CASCADE"))

        user = db.relationship('User', backref ='proclamations')
