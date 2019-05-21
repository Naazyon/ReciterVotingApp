# ReciterVotingApp
Vote for your favourite Qur'an reciter!

## Reciter Voting App
### Purpose
I've always been annoyed at the lack of ways to rate and find reciters for my holy book, the Qur'an. This is in part due to the stigma that comes from ranking systems when it comes to religious endeavours, and partly due to the fact that there are no websites or services that serve this audience. So I've decided to create a simple voting app which could rate reciters. The users can listen, login, vote, and view the results through the website, allowing everyone to easily see the best reciters for each Qur'an chapter.

I've used a simple social voting mechanism, using a simple bar graph and poll voting. Users can see what others are voting for and be persuaded to do the same. In my initial app, there were plans to implement a review and feed system, but unfortunately I ran out of time.
  
## Architecture

```
ReciterVotingApp/
├── app.db
├── config.py
├── .flaskenv
├── reciterVotingApp.py
└── app/
    ├── __init__.py
    ├── models.py
    ├── routes.py
    ├── static/
    │   ├── styles.css
    │   └── audio/
    └── templates/
        ├── base.html
        ├── chaptersList.html
        ├── navbar.html
        ├── recitersList.html
        ├── usersList.html
        ├── votePage.html
        └── votesList.html
```

The application uses Flask, HTML, Javascript and JQuery

item | description
--- | ---
app.db | This stores the database in a SQLite file
config.py | This stores all the environment variables for the program, including secret keys
.flaskenv | This sets or exports all the variables required for flask to run, including debug mode, and setting the flask file designation
reciterVotingApp.py | This starts the flask app
/app/ | Contains all the files for the application
__init.py__ | This initialises the flask app
models.py | This defines all the database models used in the application
routes.py | This defines all the routes used by flask, including POST and GET queries
/static/ | Contains all the extra files that aren't html or python files, including CSS and audio
styles.css | Contains a few global styles that are applied globally over the application
/audio/ | Contains all the audio files used in the website
/templates/ | Contains the HTML templates used in the application
base.html | The base html that all other templates inherit from
chaptersList.html | CRUD list of chapters
navbar.html | Navbar of the application
recitersList.html | CRUD list of Qur'an reciters
usersList.html | CRUD list of users
votePage.html | The html template used for voting
votesList.html | CRUD list of votes

## How to start the application

0. Ensure at minimum python3.6 is installed on your computer
1. Clone or unzip the directory to a folder on your computer
2. cd into the directory `/ReciterVotingApp/` using your terminal
3. Execute the following steps into your terminal
    3a. `pip install flask`
    3b. `pip install flask-login`
    3c. `pip install flask-sqlalchemy`
    3d. `pip install flask-migrate`
4. Set your flask environment using `export FLASK_APP=reciterVotingApp.py` or `set FLASK_APP=reciterVotingApp.py`
5. Run the app using `flask run`
