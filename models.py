
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    hardware_required = db.Column(db.String(3), nullable=True)
    os = db.Column(db.String(200), nullable=False)
    hardware = db.Column(db.String(200), nullable=False)
    # steps = db.Column(db.Text, nullable=False)
    # expected_result = db.Column(db.Text, nullable=False)
    protocol = db.Column(db.String(200), nullable=True)
    priority = db.Column(db.String(200), nullable=True)
    state = db.Column(db.String(20), default='Incomplete')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())