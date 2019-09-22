# Penn Labs Server Challenge
Remember to **document your work** in this `README.md` file! Feel free to delete these installation instructions in your fork of this repository.

## Installation
1. Fork + clone this repository. 
2. `cd` into the cloned repository.
3. Install `pipenv`
  * `brew install pipenv` if you're on a Mac.
  * `pip install --user --upgrade pipenv` for most other machines.
4. Install packages using `pipenv install`.

## Developing
1. Use `pipenv run index.py` to run the project.
2. Follow the instructions [here](https://www.notion.so/pennlabs/Server-Challenge-Fall-19-480abf1871fc4a8d9600154816726343).
3. Document your work in the `README.md` file.

## Submitting
Submit a link to your git repository to [this form](https://airtable.com/shrqdIzlLgiRFzEWh) by 11:59pm on Monday, September 23rd.

## Installing Additional Packages
To install additional packages run `pipenv install <package_name>` within the cloned repository.

## Login
> /login

Standard Login information --> username: admin password: password. Use this if you don't want to sign up. Otherwise
you can sign up with your own user and password and it will record it

## Get Club Info
> api/clubs

After you are logged in, to see the information for all clubs in json form you would hit the /api/clubs endpoint with
a get request, either using some external library or more easily just reroute the url to the base url plus the endpoint

## Create Club
> /api/clubs

After you are logged in, to create a club you would make a post request to the /api/clubs endpoint with two pieces of 
data in the payload. The payload must have a name, description, and tag key. If one of these are not present then the club
will not be created. After creating a club it will show up in subsequent get requests to the /api/clubs endpoint

## Get User info
> /api/user/<username>

After you are logged in, to get user info you would input the user's username and if it is a valid username it will return
all info stored in the database. The username must be specified in the url endpoint in the form /api/user/<username>

## Favorite a club
> /api/favorite

After you are logged in, to favorite a club you must make a post request in with the data payload has two keys: a club 
and a user key. The user and club must be valid names in order to successfully like a club. You can like any number of clubs
but you cannot like a single club more than once. 

## File upload 
> /api/clubs/forms

After you are logged in, you can use the endpoint /api/clubs/forms to upload files to clubs. The form submission page is a 
route created by one of the html templates. Currently when submitting the file it does nothing, because I have not had 
time to implement it, but further functionality is quite simple to do at this point.



