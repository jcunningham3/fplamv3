from flask import Flask, flash, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Users, Chat
from forms import UserForm, ChatForm, LoginForm
from methods import api_call, all_footballers, team, run_team, user_personal_info, classic_league, analysis, keepers, defenders, midfielders, forwards, stars
from jersey_selection import jersey_list

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///fplam'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'crow'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/logon', methods=['GET', 'POST'])
def login_route():
    form = UserForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        team_id = form.team_id.data
        run_team(email,password,team_id)
        return redirect('/')
    return render_template('login.html', form=form)

@app.route('/')
def user_page():
    info = team
    return render_template('home.html', info=info, stars=stars, jersey_list=jersey_list)
