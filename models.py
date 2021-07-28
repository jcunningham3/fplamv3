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


class Chat(db.Model):
    __tablename__ = "chat"

    league_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

class League(db.Model):
    __tablename__ = "league"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    league_id = db.Column(db.Integer, nullable=True)
