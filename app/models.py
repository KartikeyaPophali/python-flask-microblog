from app import db
from datetime import datetime

"""
Notes:-
1. SQLAlchemy automatically creates table names in 'snake_case'; eg. class name: DbTable, table name: db_table
2. Inconsistency in how table names and class names are used:
    - Note 'post = db.relationship()' statement in User class and 'user_id = db.Column()' statement in Post class
3. For one-to-many relationship, db.relationship() defined on the 'one' side
    - first arg: <ClassName> of model class representing 'many' side of the relationship
        - for a user 'u1', u1.posts will run a DB query returning all posts by 'u1'
    - backref arg: name of field added to the obj of the 'many' class; eg. post.author returns the user given a post
    - lazy arg: defines how the database query for the relationship will be issued
"""


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))   # store hash of the password - never clear string!!
    posts = db.relationship('Post', backref='author', lazy='dynamic')   # Note: 'Post' is the class name here!

    def __repr__(self):     # useful for debugging
        return f'<User> {self.username}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) # pass utcnow func, not the result (no ())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # foreign key - user.id; Note: 'user' is the table name

    def __repr__(self):
        return f'<Post {self.body}>'
