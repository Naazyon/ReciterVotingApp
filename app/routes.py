from flask import render_template
from app import app
import datetime

timeNow = datetime.datetime.now()

defaultUser = {
    'id': 1,
    'name': "Aviciena Santoso",
    'email': "22242172@student.uwa.edu.au",
    'online': timeNow.strftime('%Y-%m-%d %H:%M:%S'),
    'numVotes': 0,
    'numReviews': 0
}


@app.route('/')
@app.route('/feed')
def feed():
    return render_template('feed.html', title="Feed - QRVA")

@app.route('/overview')
def overview():
    user = {'username': 'Aviciena Santoso'}
    return render_template('overview.html', title="Overview - QRVA")

@app.route('/profile')
def profile():
    user = {'username': 'Aviciena Santoso'}
    return render_template('profile.html', title="Profile - QRVA", user=defaultUser)

@app.route('/users')
def users():
    user = {'username': 'Aviciena Santoso'}
    return render_template('users.html', title="Edit Users - QRVA")

@app.route('/vote')
def vote():
    user = {'username': 'Aviciena Santoso'}
    return render_template('vote.html', title="Edit Users - QRVA")