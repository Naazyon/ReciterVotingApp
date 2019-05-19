from app import app
from app import app, db
from app.models import User, Feed, Chapter, Review, Clip, Vote

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Feed': Feed, 'Chapter': Chapter, 'Review': Review, 'Clip': Clip, 'Vote': Vote}
