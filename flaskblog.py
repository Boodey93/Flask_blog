from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c5e6ed12174bdec5c4213e69eb22ae48'

posts = [
    {
        'author' : 'Abdelrahman Mohamed',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'October 26, 2018'
    },
    {
        'author' : 'Hoda Mohamed',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'October 27, 2018'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET','POST'])# To accept all GET & POST requests
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))#home is the function of the route not the route
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccsessful. Please check username or password', 'danger') 
    return render_template('login.html', title='Login', form=form)