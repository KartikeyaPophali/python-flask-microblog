from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Kartikeya"}
    posts = [
        {
            'author': {'username': 'Raj'},
            'body': 'Learning the Flask framework in Python for web development!'
        },
        {
            'author': {'username': 'Sid'},
            'body': 'Hope the world gets out of this pandemic soon.'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
