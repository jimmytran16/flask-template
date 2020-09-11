# How to set up the template
This is a basic template for next Flask application

## Local
Make sure you have [Python](https://www.python.org/downloads/) installed.

```sh
$ git clone https://github.com/jimmytran16/flask-template.git
$ cd flask-template
$ pip install -r requirements.txt
$ python server.py
```
Your app should now be running on [localhost:5000](http://localhost:5000/).

## If you want to deploy to Heroku (Using CLI)
 Make sure you have [Heroku CLI](https://cli.heroku.com/) installed.

```
$ heroku create <your-project-name>
$ git push heroku master
$ heroku open
```
or

## Deploy on the browser
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
