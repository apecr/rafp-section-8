from app import app
from db import db

db.init_app(app)


@app.before_first_request
def init_bbdd():
    db.create_all()
