from flask import render_template, request, send_from_directory, redirect, url_for
from app import app, db
from app.models import User, Chapter, Reciter, Vote
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash
import datetime
import json

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/userslist')
def usersList():
  users = User.query.all()
  return render_template('usersList.html', users=users)

@app.route('/chapterslist')
def chaptersList():
  return render_template('chapterslist.html')

@app.route('/recitersList')
def recitersList():
  return render_template('recitersList.html')

@app.route('/votesList')
def votesList():
  return render_template('votesList.html')

@app.route('/user', methods=['POST'])
def user():
  if(request.form):
    print(request.form)
    if(request.form["type"] == "CREATE"):
      permissions = request.form["permissions"]
      name = request.form["name"]
      email = request.form["email"]
      password = generate_password_hash(request.form["password"])
      user = User(
        permissions = permissions,
        name = name,
        email = email,
        password = password
      )
      db.session.add(user)
      db.session.commit()
      return redirect('/')
    if(request.form["type"] == "UPDATE"):
      id = request.form["id"]
      if id is not None and id != 0:
        user = User.query.get(id)
        if user:
          user.permissions = request.form["permissions"]
          user.name = request.form["name"]
          user.email = request.form["email"]
          user.password = generate_password_hash(request.form["password"]) or user.password
          db.session.commit()
          return redirect('/')
    if(request.form["type"] == "DELETE"):
      id = request.form["id"]
      if id is not None and id != 0:
        user = User.query.get(id)
        if user:
          db.session.delete(user)
          db.session.commit()
          return redirect('/')
  return "invalid request"

@app.route('/chapter')
def chapter():
  if(request.form):
    print(request.form)
  return "invalid request"

@app.route('/reciter')
def reciter():
  if(request.form):
    print(request.form)
  return "invalid request"

@app.route('/vote')
def vote():
  if(request.form):
    print(request.form)
  return "invalid request"

"""
timeNow = datetime.datetime.now()

quranChapters = [ { "id": 1, "name": "Al-Fatihah", "translation": "The Opening" }, { "id": 2, "name": "Al-Baqarah", "translation": "The Calf" }, { "id": 3, "name": "Al Imran", "translation": "The Family of�Imran" }, { "id": 4, "name": "An-Nisa'", "translation": "The Women" }, { "id": 5, "name": "Al-Ma'idah", "translation": "The Food" }, { "id": 6, "name": "Al-An'am", "translation": "The Cattle" }, { "id": 7, "name": "Al-A'raf", "translation": "The Heights" }, { "id": 8, "name": "Al-Anfal", "translation": "The Spoils of War" }, { "id": 9, "name": "At-Tawbah", "translation": "The Repentance" }, { "id": 10, "name": "Yunus", "translation": "Yunus" }, { "id": 11, "name": "Hud", "translation": "Hud" }, { "id": 12, "name": "Yusuf", "translation": "Joseph" }, { "id": 13, "name": "Ar-Ra'd", "translation": "The Thunder" }, { "id": 14, "name": "Ibraheem", "translation": "Abraham" }, { "id": 15, "name": "Al-Hijr", "translation": "The Rocky Tract" }, { "id": 16, "name": "An-Nahl", "translation": "The Honey Bees" }, { "id": 17, "name": "Al-Isra", "translation": "The Night Journey" }, { "id": 18, "name": "Al-Kahf", "translation": "The Cave" }, { "id": 19, "name": "Maryam", "translation": "Mary" }, { "id": 20, "name": "Ta-Ha", "translation": "Ta-Ha" }, { "id": 21, "name": "Al-Anbiya'", "translation": "The Prophets" }, { "id": 22, "name": "Al-Hajj", "translation": "The Pilgrimage" }, { "id": 23, "name": "Al-Mu'minoon", "translation": "The Believers" }, { "id": 24, "name": "An-Nur", "translation": "The Light" }, { "id": 25, "name": "Al-Furqan", "translation": "The Criterion" }, { "id": 26, "name": "ash-Shu`ara'", "translation": "The Poets" }, { "id": 27, "name": "An-Naml", "translation": "The Ant" }, { "id": 28, "name": "Al-Qasas", "translation": "The Narrations" }, { "id": 29, "name": "Al-`Ankabut", "translation": "The Spider" }, { "id": 30, "name": "Ar-Rum", "translation": "The Romans" }, { "id": 31, "name": "Luqman", "translation": "Luqman" }, { "id": 32, "name": "As-Sajdah", "translation": "The Prostration" }, { "id": 33, "name": "Al-Ahzab", "translation": "The Clans" }, { "id": 34, "name": "Saba'", "translation": "Sheba" }, { "id": 35, "name": "Fatir", "translation": "The Originator" }, { "id": 36, "name": "Yaseen", "translation": "Yaseen" }, { "id": 37, "name": "As-Saffat", "translation": "Those Who Set The Ranks" }, { "id": 38, "name": "Sad", "translation": "Sad" }, { "id": 39, "name": "Az-Zumar", "translation": "The Crowds" }, { "id": 40, "name": "Ghafir", "translation": "The Forgiver (God)" }, { "id": 41, "name": "Fussilat", "translation": "Expounded" }, { "id": 42, "name": "Ash-Shura", "translation": "The Consultation" }, { "id": 43, "name": "Az-Zukhruf", "translation": "The Gold Adornments" }, { "id": 44, "name": "Ad-Dukhan", "translation": "The Smoke" }, { "id": 45, "name": "Al-Jathiyah", "translation": "The Kneeling Down" }, { "id": 46, "name": "Al-Ahqaf", "translation": "Winding Sand-tracts" }, { "id": 47, "name": "Muhammad", "translation": "Muhammad" }, { "id": 48, "name": "Al-Fath", "translation": "The Victory" }, { "id": 49, "name": "Al-Hujurat", "translation": "The Private Apartments" }, { "id": 50, "name": "Qaf", "translation": "Qaf" }, { "id": 51, "name": "Ad-Dhariyat", "translation": "The Wind That Scatter" }, { "id": 52, "name": "At-Tur", "translation": "The Mount" }, { "id": 53, "name": "An-Najm", "translation": "The Star" }, { "id": 54, "name": "Al-Qamar", "translation": "The Moon" }, { "id": 55, "name": "Ar-Rahman", "translation": "The Most Merciful" }, { "id": 56, "name": "Al-Waqi'ah", "translation": "The Inevitable" }, { "id": 57, "name": "Al-Hadeed", "translation": "The Iron" }, { "id": 58, "name": "Al-Mujadilah", "translation": "The Pleading" }, { "id": 59, "name": "Al-Hashr", "translation": "The Mustering" }, { "id": 60, "name": "Al-Mumtahanah", "translation": "The Examined One" }, { "id": 61, "name": "As-Saff", "translation": "The Ranks" }, { "id": 62, "name": "Al-Jumu'ah", "translation": "The Congregation" }, { "id": 63, "name": "Al-Munafiqun", "translation": "The Hypocrites" }, { "id": 64, "name": "At-Taghabun", "translation": "The Cheating" }, { "id": 65, "name": "At-Talaq", "translation": "Divorce" }, { "id": 66, "name": "At-Tahreem", "translation": "The Prohibition" }, { "id": 67, "name": "Al-Mulk", "translation": "The Dominion" }, { "id": 68, "name": "Al-Qalam", "translation": "The Pen" }, { "id": 69, "name": "Al-Haqqah", "translation": "The Sure Reality" }, { "id": 70, "name": "Al-Ma'aarij", "translation": "The Ways of Ascent" }, { "id": 71, "name": "Nuh", "translation": "Noah" }, { "id": 72, "name": "Al-Jinn", "translation": "The Spirits" }, { "id": 73, "name": "Al-Muzzammil", "translation": "The Enfolded One" }, { "id": 74, "name": "Al-Muddathir", "translation": "The One Wrapped Up" }, { "id": 75, "name": "Al-Qiyamah", "translation": "Resurrection" }, { "id": 76, "name": "Al-Insan", "translation": "The Human" }, { "id": 77, "name": "Al-Mursalat", "translation": "Those Sent Forth" }, { "id": 78, "name": "An-Naba'", "translation": "The Great News" }, { "id": 79, "name": "An-Nazi'at", "translation": "Those Who Tear Out" }, { "id": 80, "name": "`Abasa", "translation": "He Frowned" }, { "id": 81, "name": "At-Takweer", "translation": "The Folding Up" }, { "id": 82, "name": "Al-Infitar", "translation": "The Cleaving Asunder" }, { "id": 83, "name": "Al-Mutaffifeen", "translation": "The Dealers in Fraud" }, { "id": 84, "name": "Al-Inshiqaq", "translation": "The Rending Asunder" }, { "id": 85, "name": "Al-Burooj", "translation": "The Mansions Of The Stars" }, { "id": 86, "name": "At-Tariq", "translation": "The Night-Visitant" }, { "id": 87, "name": "Al-A'la", "translation": "The Most High" }, { "id": 88, "name": "Al-Ghashiyah", "translation": "The Overwhelming Event" }, { "id": 89, "name": "Al-Fajr", "translation": "The Break of Day" }, { "id": 90, "name": "Al-Balad", "translation": "The City" }, { "id": 91, "name": "Ash-Shams", "translation": "The Sun" }, { "id": 92, "name": "Al-Lail", "translation": "The Night" }, { "id": 93, "name": "Ad-Dhuha", "translation": "The Glorious Morning Light" }, { "id": 94, "name": "Al-Inshirah", "translation": "The Expansion of Breast" }, { "id": 95, "name": "Al-Teen", "translation": "The Fig Tree" }, { "id": 96, "name": "al-`Alaq", "translation": "The Clinging Clot" }, { "id": 97, "name": "Al-Qadr", "translation": "The Night of Honor" }, { "id": 98, "name": "Al-Bayyinah", "translation": "The Clear Evidence" }, { "id": 99, "name": "Az-Zalzala", "translation": "The Earthquake" }, { "id": 100, "name": "Al-Adiyat", "translation": "The Courser" }, { "id": 101, "name": "al-Qari`ah", "translation": "The Striking Hour" }, { "id": 102, "name": "At-Takathur", "translation": "The Piling Up" }, { "id": 103, "name": "Al-Asr", "translation": "The Time" }, { "id": 104, "name": "Al-Humazah", "translation": "The Scandalmonger" }, { "id": 105, "name": "Al-Feel", "translation": "The Elephant" }, { "id": 106, "name": "Quraish", "translation": "Quraysh" }, { "id": 107, "name": "Al-Maa'oun", "translation": "The Neighbourly Assistance" }, { "id": 108, "name": "Al-Kawthar", "translation": "Abundance" }, { "id": 109, "name": "Al-Kafiroun", "translation": "The Disbelievers" }, { "id": 110, "name": "An-Nasr", "translation": "The Help" }, { "id": 111, "name": "Al-Masad", "translation": "The Plaited Rope" }, { "id": 112, "name": "Al-Ikhlas", "translation": "Purity of Faith" }, { "id": 113, "name": "Al-Falaq", "translation": "The Daybreak" }, { "id": 114, "name": "Al-Nas", "translation": "Mankind" } ]

@app.route('/', methods=["GET", "POST"])
@app.route('/feed')
def feed():
  if(request):
    print(request.form)
  return render_template('feed.html', title="Feed - QRVA")

@app.route('/overview', methods=["GET", "POST"])
def overview():
  if(request):
    print(request.form)
  return render_template('overview.html', title="Overview - QRVA")

@app.route('/profile', methods=["GET", "POST"])
def profile():
  if(request):
    print(request.form)
  return render_template('profile.html', title="Profile - QRVA")

@app.route('/users', methods=["GET", "POST"])
def users():
  if(request):
    print(request.form)
  return render_template('users.html', title="Edit Users - QRVA")

@app.route('/chapters', methods=["GET", "POST"])
def chapters():
  if(request):
    print(request.form)
  return render_template('chapters.html', title="Edit Chapters - QRVA")

@app.route('/vote/<int:chapter>', methods=["GET", "POST"])
def vote(chapter):
  if(request.form):
    print(request.form)
    currentVote = Vote(reciter = request.form["reciter"],
    chapter = request.form["chapter"],
    user = request.form["user"],
    upvote = request.form["upvote"])
    db.session.add(currentVote)
    db.session.commit()
  currentChapter = quranChapters[chapter-1]
  currentReviews = Review.query.filter_by(chapter=chapter).all()
  return render_template('vote.html', title="Vote - QRVA", chapter = currentChapter, reviews = currentReviews)

@app.route('/review', methods=["GET", "POST"])
def review():
  if(request.form):
  print(request.form)
  currentReview = Review(reciter = request.form["reciter"],
  chapter = request.form["chapter"],
  user = request.form["user"],
  content = request.form["content"],
  rating = request.form["rating"])
  db.session.add(currentReview)
  db.session.commit()
  print("Review added!")
  return redirect(url_for('feed'))
  return redirect(url_for('feed'))

@app.route('/user', methods=["POST", "GET"])
  if(request.form):
  print(request.form)
  if(request.form["type"] == "create"){
  }
  if(request.form["type"] == "update"){
  }
  if(request.form["type"] == "delete"){
  }

@app.route('/static/<path:path>')
def sendFiles(path):
  if(request):
    print(request.form)
  return send_from_directory('static/', path)

@app.route('/audio/<path:path>')
def sendAudio(path):
  if(request):
    print(request.form)
  return send_from_directory('static/audio/', path)

@app.route('/login', methods=["GET", "POST"])
def login():
  if(request.form):
    print(request.form)
    email = request.form['email']
    password = request.form['password']
    if current_user.is_authenticated:
      print(f"User {current_user.email} already authenticated.")
      return redirect(url_for('feed'))
    currentUser = User.query.filter_by(email=email).first()
    if currentUser is None:
      print('Email not found')
      return redirect(url_for('feed'))
    if not currentUser.check_password(password):
      print('Password incorrect')
      return redirect(url_for('feed'))
    login_user(currentUser)
    print(f'User {currentUser.email} logged in.')
    return redirect(url_for('feed'))
  else:
    return redirect(url_for('feed'))

@app.route('/logout', methods=["GET", "POST"])
def logout():
  logout_user()
  print("Logged out.")
  return redirect(url_for('feed'))

@app.route('/register', methods=["GET", "POST"])
def register():
  if(request.form):
    print(request.form)
    email = request.form['email']
    password = generate_password_hash(request.form['password'])
    permissions = "user"
    name = "John Doe"
    user = User(email=email,
    password=password,
    permissions=permissions,
    name=name)
    db.session.add(user)
    db.session.commit()
    print("Database user added!")
  return redirect(url_for('feed'))

"""


if __name__ == "__main__":
  app.run()