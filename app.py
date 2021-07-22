from flask import Flask, flash, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from methods import api_call, all_footballers, team, run_team, user_personal_info, classic_league, analysis, keepers, defenders, midfielders, forwards, stars

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'crow'
toolbar = DebugToolbarExtension(app)

@app.route('/')
def home():
    run_team()
    info = team
    return render_template('home.html', info=info, stars=stars)
