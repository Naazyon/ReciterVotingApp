from flask import render_template
from app import app
import datetime

@app.route('/')
@app.route('/home')
def home():
    user = {'username': 'Aviciena Santoso'}
    return render_template('home.html', user=user)