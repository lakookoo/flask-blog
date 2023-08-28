from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fb3b44081c45e4e93bd62d6b377af670'
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
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form )

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form )

if __name__ == '__main__':
    app.run(debug=True)