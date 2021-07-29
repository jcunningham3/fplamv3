from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    team_id = db.Column(db.Integer, nullable=False)
    classic_id = db.Column(db.Integer, nullable=True)

    @classmethod
    def authenticate(cls, email):
        u = Users.query.filter_by(email=email).first()

        if u:
            return u
        else:
            return False


class Chat(db.Model):
    __tablename__ = "chat"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('Users', backref='chat')
