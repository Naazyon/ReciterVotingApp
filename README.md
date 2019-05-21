# ReciterVotingApp
Vote for your favourite Qur'an reciter!

## Reciter Voting App
### Purpose
I've always been annoyed at the lack of ways to rate and find reciters for my holy book, the Qur'an. This is in part due to the stigma that comes from ranking systems when it comes to religious endeavours, and partly due to the fact that there are no websites or services that serve this audience. So I've decided to create a simple voting app which could rate reciters. The users can listen, login, vote, and view the results through the website, allowing everyone to easily see the best reciters for each Qur'an chapter.
I've used a simple social voting mechanism, using a simple bar graph and poll voting.
  
## Architecture

```
ReciterVotingApp/
├── app.db
├── config.py
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

## describe how to launch the web application.
## Include commit logs, showing contributions and review from both contributing students
