from sqlite3 import Connection

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


@event.listens_for(Engine, "connect")
def set_sqlite_foreign_keys_on_connect(dbapi_connection, _connection_record):
    """Enable foreign key constraints on the database connections."""
    if not isinstance(dbapi_connection, Connection):
        return

    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)

    appearances = db.relationship('Appearance',
                                  backref='episode',
                                  cascade='all, delete-orphan')
    guests = association_proxy('appearances', 'guest')

    def __repr__(self):
        return f'Episode(date="{self.date}"), number=({self.number})'


class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    episode_id = db.Column(db.Integer,
                           db.ForeignKey('episodes.id'),
                           nullable=False)
    guest_id = db.Column(db.Integer,
                         db.ForeignKey('guests.id'),
                         db.ForeignKey('guests.id'),
                         nullable=False)

    __table_args__ = UniqueConstraint('episode_id',
                                      'guest_id',
                                      name='uq_episode_id_guest_id'),

    serialize_rules = '-episode.appearances', '-guest.appearances'

    @validates('rating')
    def validate_rating(self, _, rating):
        """
        Validate the rating of an Appearance.

        Raises:
            ValueError: If the rating is not between 1 and 5.
        """
        if rating < 1 or rating > 5:
            raise ValueError(
                'Invalid rating. Rating should be between 1 and 5.')
        return rating

    def __repr__(self):
        return f'Appearance(rating={self.rating}, episode_id={self.episode_id}, guest_id={self.guest_id})'


class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    appearances = db.relationship('Appearance',
                                  backref='guest',
                                  cascade='all, delete-orphan')
    episodes = association_proxy('appearances', 'episode')

    def __repr__(self):
        return f'Guest(name="{self.name}", occupation="{self.occupation}")'