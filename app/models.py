
from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(120), index=True, unique=True)
    start = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    password_hash = db.Column(db.String(128))

    def __init__(self, task, description, ):
        self.task = task
        self.description = description

    def __repr__(self):
        return '<Task {}>'.format(self.task)

db.create_all()

