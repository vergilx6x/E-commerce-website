#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.product import Product
from models.category import Category
from models.user import User
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
# app.jinja_env.trim_block
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/home', strict_slashes=False)
def home():
    """ displays a HTML page with a list of states """
    products = storage.all(Product).values()
    # products = sorted(products, key=lambda k: k.name)
    categories = storage.all(Category).values()
    return render_template('home.html', categories=categories, new_products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(email=email, password=hashed_password, username=username)
        
        try:
            
            storage.new(new_user)
            storage.save
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        except:
            storage.rollback()
            flash('Registration failed. Username or email may already be taken.', 'error')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = storage.get_user(username)
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and/or password.', 'error')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        return render_template('dashboard.html', user=user)
    return render_template('dashboard.html', user=user)
if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)