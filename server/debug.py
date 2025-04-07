# debug.py
from app import app
from models import db, Guest, Episode, Appearance

with app.app_context():
    print("Number of Guests:", Guest.query.count())
    print("First 5 guests:")
    for guest in Guest.query.limit(5).all():
        print(guest.name, "-", guest.occupation)