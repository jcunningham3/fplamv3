from flask import Flask, flash, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Users, Chat, League
from forms import UserForm, ChatForm, LoginForm
from methods import api_call, all_footballers, team, run_team, user_personal_info, classic_league, analysis, keepers, defenders, midfielders, forwards, stars
from jersey_selection import jersey_list
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///fplam')#.replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'crowBottom')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

# home route
@app.route('/')
def home_route():
    return render_template('/home.html')

# register route
@app.route('/register', methods=['GET', 'POST'])
def register_route():
    form = UserForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        team_id = form.team_id.data
        run_team(email,password,team_id)

        new_user = Users(email=email, team_id=team_id)
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        info = team
        flash(f"Welcome {info['user_info']['name']}")
        return redirect('/user')
    return render_template('register.html', form=form)

# logging in
@app.route('/logon', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        team_id = form.team_id.data
        # user = Users.authenticate(email)
        #if user:
            #session['user_id'] = user.id
        run_team(email,password,team_id)
        return redirect('/user')
        #else:
            #form.email.errors = ['Invalid email/password.']
    return render_template('login.html', form=form)

# user route
@app.route('/user')
def user_page():
    info = team
    return render_template('user.html', info=info, stars=stars, jersey_list=jersey_list)

# logging out
@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')
