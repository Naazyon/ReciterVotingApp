from app import app
import datetime

@app.route('/')
@app.route('/home')
def index():
    return f"Hello world! --- Initial commit for UWA CITS3403 Assignment. --- Name: Aviciena Santoso --- The time is {datetime.datetime.now()}"
