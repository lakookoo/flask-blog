from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm

posts = [
    {
        'author':'Larisa',
        'title':'post 1',
        'content':'content 1',
        'date_posted':'April 1, 2023',
    },
    {
        'author':'Larisa Kisa',
        'title':'post 2',
        'content':'content 2',
        'date_posted':'April 21, 2023',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', '_success_')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form )

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Log in {form.username.data}!', '_success_')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form )