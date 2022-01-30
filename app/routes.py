from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


# view functions mapped to different URLs

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Kartikeya"}  # mock user
    posts = [                         # mock posts
        {
            'author': {'username': 'Raj'},
            'body': 'Learning the Flask framework in Python for web development!'
        },
        {
            'author': {'username': 'Sid'},
            'body': 'Hope the world gets out of this pandemic soon.'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)  # invokes Jinja2's template engine


@app.route('/login', methods=['GET', 'POST'])   # default .route accepts only GET, for others shows 'Method Not Allowed'
def login():
    form = LoginForm()
    # form.validate_on_submit() returns False for a GET request, so control directly goes to the last return statement
    # method returns True for a POST request if ALL fields pass the validation, else False
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))   # url_for('<url>') better than '/<html_file>' - handles dynamic components
    return render_template('login.html', title='Sign In', form=form)
