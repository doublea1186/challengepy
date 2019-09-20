from flask import Flask, request
from scraper import * # Web Scraping utility functions for Online Clubs with Penn.
from club import *
app = Flask(__name__)

@app.route('/')
def main():
    html = get_clubs_html()
    soup = soupify(html)
    y = get_clubs(soup)
    clubs = create_clubs_array(y)
    save_club_info(clubs)
    return "Welcome to Penn Club Review!"

@app.route('/api')
def api():
    return "Welcome to the Penn Club Review API!."

if __name__ == '__main__':
    app.run()
