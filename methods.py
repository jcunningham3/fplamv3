import requests

# make a user profile to collect all the necessary data and import the profile into app.py
team = {
    'my_picks': [],
    'all_player_data': [],
    'user_info': [],
    'league_info': [],
    'stars': []
}

keepers = []
defenders = []
midfielders = []
forwards = []
stars = []

# fpl endpoint needing authorization for team info
def api_call(email, password, team_id):
    team_id = str(team_id)
    # put the cookies received in session to be remembered
    session = requests.session()

    # url needed to make the post request
    url = 'https://users.premierleague.com/accounts/login/'

    # data needed for the post request
    payload = {
     'password': password,
     'login': email,
     'redirect_uri': 'https://fantasy.premierleague.com/a/login',
     'app': 'plfpl-web'
    }
    session.post(url, data=payload)

    # Get response sent with authorization cookies
    res = session.get('https://fantasy.premierleague.com/api/my-team/' + team_id + '/')

    # setting the response to a var called 'data' and making the response json
    data = res.json()

    team['my_picks'] = data['picks']

# fpl endpoint with player data
def all_footballers():
    res = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    data = res.json()
    data = data['elements']
    team['all_player_data'] = data

# fpl user personal info
def user_personal_info(team_id):
    team_id = str(team_id)
    res = requests.get('https://fantasy.premierleague.com/api/entry/' + team_id + '/')
    data = res.json()
    team['user_info'] = data

# get request for users classic league information
def classic_league(id):
    if id == 0:
        return 'user is not participating in a classic league'
    else:
        id = str(id)
        res = requests.get('https://fantasy.premierleague.com/api/leagues-classic/'+ id + '/standings/')
        data = res.json()
        team['league_info'] = data

# sorting function that seperates all players by position
def analysis():
    # make the lists needed global
    global keepers
    global defenders
    global midfielders
    global forwards
    global stars
    # iterate over all th eplayers in the fpl
    for player in team['all_player_data']:
        # find all the keepers
        if player['element_type'] == 1:
            # put all the keepers in the keeper list
            keepers.append(player)

        # find all the defenders
        if player['element_type'] == 2:
            # put all the defenders in the keeper list
            defenders.append(player)

        # find all the midfielders
        if player['element_type'] == 3:
            # put all the midfielders in the keeper list
            midfielders.append(player)

        # find all the forwards
        if player['element_type'] == 4:
            # put all the forwards in the keeper list
            forwards.append(player)

    # sort each list in descending order
    keepers = sorted(keepers, key=lambda i: (i['total_points']), reverse=True)
    defenders = sorted(defenders, key=lambda i: (i['total_points']), reverse=True)
    midfielders = sorted(midfielders, key=lambda i: (i['total_points']), reverse=True)
    forwards = sorted(forwards, key=lambda i: (i['total_points']), reverse=True)

    # append the top players from each list into the star list
    stars.append(keepers[0])
    stars.append(keepers[1])
    stars.append(defenders[0])
    stars.append(defenders[1])
    stars.append(defenders[2])
    stars.append(defenders[3])
    stars.append(defenders[4])
    stars.append(midfielders[0])
    stars.append(midfielders[1])
    stars.append(midfielders[2])
    stars.append(midfielders[3])
    stars.append(midfielders[4])
    stars.append(forwards[0])
    stars.append(forwards[1])
    stars.append(forwards[2])

    #sort the star list in descending order
    stars = sorted(stars, key=lambda i: (i['total_points']), reverse=True)

# run all the functions to create the team profile
def run_team(email,password,team_id):
    api_call(email,password,team_id)
    all_footballers()
    user_personal_info(team_id)
    analysis()

# 'cunheez3@gmail.com', 'Tottenham7', 307976
# 'jan6person@hotmail.com', 'Winter2011', 709137
# 'fplexampleman@gmail.com', 'Tottenham7', 1583773

# api_call('jan6person@hotmail.com', 'Winter2011', 709137)
# print(team['my_picks']['picks'])
