from flask import render_template
from app import app
import datetime

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
    return render_template('profile.html', title="Profile - QRVA")

@app.route('/users')
def users():
    user = {'username': 'Aviciena Santoso'}
    return render_template('users.html', title="Edit Users - QRVA")

@app.route('/vote')
def vote():
    user = {'username': 'Aviciena Santoso'}
    return render_template('users.html', title="Edit Users - QRVA")