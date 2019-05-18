from flask import render_template, request, send_from_directory
from app import app
import datetime

timeNow = datetime.datetime.now()

surahs = [[67 ,"Al-Mulk"], [68 ,"Al-Qalam"], [69 ,"Al-Haqqah"], [70 ,"Al-Ma'aarij"], [71 ,"Nuh"], [72 ,"Al-Jinn"], [73 ,"Al-Muzzammil"], [74 ,"Al-Muddathir"], [75 ,"Al-Qiyamah"], [76 ,"Al-Insan"], [77 ,"Al-Mursalat"], [78 ,"An-Naba'"], [79 ,"An-Nazi'at"], [80 ,"`Abasa"], [81 ,"At-Takweer"], [82 ,"Al-Infitar"], [83 ,"Al-Mutaffifeen"], [84 ,"Al-Inshiqaq"], [85 ,"Al-Burooj"], [86 ,"At-Tariq"], [87 ,"Al-A'la"], [88 ,"Al-Ghashiyah"], [89 ,"Al-Fajr"], [90 ,"Al-Balad"], [91 ,"Ash-Shams"], [92 ,"Al-Lail"], [93 ,"Ad-Dhuha"], [94 ,"Al-Inshirah"], [95 ,"Al-Teen"], [96 ,"al-`Alaq"], [97 ,"Al-Qadr"], [98 ,"Al-Bayyinah"], [99 ,"Az-Zalzala"], [100,"Al-Adiyat"], [101,"al-Qari`ah"], [102,"At-Takathur"], [103,"Al-Asr"], [104,"Al-Humazah"], [105,"Al-Feel"], [106,"Quraish"], [107,"Al-Maa'oun"], [108,"Al-Kawthar"], [109,"Al-Kafiroun"], [110,"An-Nasr"], [111,"Al-Masad"], [112,"Al-Ikhlas"], [113,"Al-Falaq"], [114,"Al-Nas"]]

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

@app.route('/vote/<int:chapter>')
def vote(chapter):
    user = {'username': 'Aviciena Santoso'}
    if chapter >= 100:
        chapter = str(chapter)
    elif chapter >= 10:
        chapter = f'0{chapter}'
    else:
        chapter = f'00{chapter}'
    return render_template('vote.html', title="Vote - QRVA", chapter = chapter, user = defaultUser)

@app.route('/audio/<path:path>')
def sendAudio(path):
    return send_from_directory('static/audio/', path)

if __name__ == "__main__":
    app.run()