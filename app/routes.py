from flask import render_template
from app import app
import datetime

@app.route('/')
@app.route('/feed')
def feed():
    user = {'username': 'Aviciena Santoso'}
    return render_template('feed.html', title="Feed - QRVA", user=user)