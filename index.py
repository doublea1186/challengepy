from flask import Flask, flash, render_template, request, session
from scraper import * # Web Scraping utility functions for Online Clubs with Penn.
from user import *
import requests
import json
import os
from unitTests import *
app = Flask(__name__)

#uncomment these lines if you would like to reinitialize the club list and user database
#init_clubs()
#User("", "", "", "").init_users()


@app.route('/')
def home():
    app.secret_key = os.urandom(12)
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"


@app.route('/signup', methods=["POST"])
def signup():
    name = request.form['name']
    user = request.form['username']
    password = request.form['password']
    new_user = User(name, user, password, 0)
    current_user = new_user.save_user()

    if current_user:
        session['logged_in'] = True
        return "your info has been saved"
    else:
        return render_template('login.html')


@app.route('/login', methods=['POST', "GET"])
def do_admin_login():
    user = request.form['username']
    password = request.form['password']
    user = User("", user, password, 0)

    if user.authenticate():
        session['logged_in'] = True
        return "HI"
    else:
        flash('wrong password!')
        return render_template('login.html')


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


@app.route('/forward/signup', methods=["POST"])
def forward_signup():
    return render_template('signup.html')


@app.route('/forward/login', methods=["POST"])
def forward_login():
    return render_template('login.html')


@app.route('/api')
def api():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Welcome to the Penn Club Review API!."


@app.route('/api/clubs', methods=["GET","POST"])
def api_clubs():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        create_club()
        clubs = read_club_info()
        if request.method == "GET":
            json_string = json.dumps(clubs, default=obj_dict)
            return json_string

        else:
            name = request.form['name']
            description = request.form['description']
            tags = requests.form['tags']
            clubs.append(Club(name, description, tags, 0))
            save_club_info(clubs)


@app.route('/api/clubs/forms/', methods=["GET", "POST"])
def api_clubs_forms():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == "GET":
            return render_template('upload.html')
        else:
            name = request.form['club name']
            file = request.form['file']
            return "MONKEY"


@app.route('/api/user/<username>', methods=["GET"])
def api_user(username):
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == "GET":
            user = User("", username, "", 0)
            all_users = user.read_user_data()

            for user in all_users:
                if user.user.lower() == username.lower():
                    return json.dumps(user, default=obj_dict)
            return "NO USER FOUND"


@app.route('/api/favorite', methods=["POST"])
def api_favorite():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == "POST":
            club = request.form['club']
            user = User("", request.form['user'], "", "")
            all_users = user.read_user_data()
            user_index = user.find_user_index()

            if not all_users[user_index] & user_index != -1:
                likes = all_users[user_index].get_likes
                for like in likes:
                    if like == club:
                        return
                    else:
                        previous_clubs = all_users[user_index].get_likes();
                        previous_clubs.append(club)
                        all_users[user_index].set_likes(previous_clubs)
                        with open('user.info', 'wb') as config_file:
                            pickle.dump(all_users, config_file)

                        all_clubs = read_club_info()
                        club_index = get_club_index(club)

                        if club_index != -1:
                            all_clubs[club_index].set_likes(all_clubs[club_index].get_likes() + 1)
                            with open('clubsInfo.club', 'wb'):
                                pickle.dump(all_clubs)

                            return "Your favorite club has been recorded"


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
