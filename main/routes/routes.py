from main import app
from flask import render_template

@app.route('/') #the routing to the main page
def home():
    return render_template('index.html')
