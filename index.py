from flask import Flask, flash, redirect, render_template, request, session, abort
from scraper import * # Web Scraping utility functions for Online Clubs with Penn.
import json
import os

app = Flask(__name__)


@app.route('/')
def home():
    app.secret_key = os.urandom(12)
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"

# @app.route('/signup', methods=['POST'])
# def signup():
#     if not session['logged_in']:
#         username = request.form['username']
#         password = request.form['password']
#         return username


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return "HI"
    else:
        flash('wrong password!')
        return home()


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


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
        clubs = read_club_info()
        if request.method == "GET":
            json_string = json.dumps(clubs, default=obj_dict)
            return json_string

        else:
            name = request.data.name
            description = request.description
            tags = requests.description
            clubs.append(Club(name, description, tags, 0))
            save_club_info(clubs)


@app.route('/api/user/<username>', methods=["GET"])
def api_user(username):
    if not session.get('logged_in'):
        return render_template('login.html')
    if request.method == "GET":
        return username


@app.route('/api/favorite', methods=["POST"])
def api_favorite():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == "POST":
            return "API FAVORITE"


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
