from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)