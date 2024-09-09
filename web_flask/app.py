#!/usr/bin/python3
""" Starts a Flask Web Application """

from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import storage
from models.product import Product
from models.category import Category
from models.user import User
from models.cart import Cart
from models.cart_item import Cart_item
from models.favorite import Favorite

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/home', strict_slashes=False)
def home():
    """ Displays a HTML page with a list of products and categories """
    products = storage.all(Product).values()
    categories = storage.all(Category).values()
    trending_products = []  # Add logic to fetch trending products if needed
    return render_template('home.html', categories=categories, new_products=products, trending_products=trending_products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Register a new user """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(email=email, password=hashed_password, username=username)
        
        try:
            storage.new(new_user)
            storage.save()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            storage.rollback()
            flash(f'Registration failed. Error: {e}', 'error')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Log in an existing user """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = storage.get_user(username)
        print(user)
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and/or password.', 'error')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """ Display the user dashboard """
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        return render_template('dashboard.html', user=user)
    else:
        flash('You need to log in to access the dashboard.', 'warning')
        return redirect(url_for('login'))

@app.route('/cart')
def cart():
    """ Display the user's shopping cart """
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            cart_items = storage.all(Cart_item)
            user_cart_items = [item for item in cart_items.values() if item.cart.user_id == user.id]
            return render_template('cart.html', cart_items=user_cart_items)
        else:
            flash('User not found. Please log in again.', 'error')
            return redirect(url_for('login'))
    else:
        flash('You need to log in to access the cart.', 'warning')
        return redirect(url_for('login'))

@app.route('/favorites')
def favorites():
    """ Display the user's favorite products """
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        favorite_items = storage.all(Favorite)
        user_favorites = [item for item in favorite_items.values() if item.user_id == user.id]
        return render_template('favorites.html', favorite_items=user_favorites)
    else:
        flash('You need to log in to access favorites.', 'warning')
        return redirect(url_for('login'))

@app.route('/user_profile')
def user_profile():
    """ Display the user's profile """
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        return render_template('user_profile.html', user=user)
    else:
        flash('You need to log in to access your profile.', 'warning')
        return redirect(url_for('login'))

@app.route('/remove_from_cart/<string:product_id>')
def remove_from_cart(product_id):
    """ Remove a product from the cart """
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            cart_item = next((item for item in storage.all(Cart_item).values() if item.product_id == product_id and item.cart.user_id == user.id), None)
            if cart_item:
                storage.delete(cart_item)
                storage.save()
                flash('Product removed from cart.', 'success')
            else:
                flash('Product not found in cart.', 'error')
        else:
            flash('User not found. Please log in again.', 'error')
        return redirect(url_for('cart'))
    else:
        flash('You need to log in to remove items from your cart.', 'warning')
        return redirect(url_for('login'))
    
@app.route('/add_to_cart/<string:product_id>', methods=['POST'])
def add_to_cart(product_id):
    """ Add a product to the cart """
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            product = storage.get(Product, product_id)
            if product:
                # Find or create a cart for the user
                user_cart = next((cart for cart in storage.all(Cart).values() if cart.user_id == user.id), None)
                
                if not user_cart:
                    # Create a new cart if one does not exist for the user
                    user_cart = Cart(user_id=user.id)
                    storage.new(user_cart)
                    storage.save()

                # Check if the product is already in the user's cart
                existing_item = next((item for item in storage.all(Cart_item).values() if item.product_id == product_id and item.cart_id == user_cart.id), None)
                
                if existing_item:
                    flash('Product already in cart.', 'info')
                else:
                    # Add the product to the cart
                    new_cart_item = Cart_item(cart_id=user_cart.id, product_id=product_id)
                    storage.new(new_cart_item)
                    storage.save()
                    flash('Product added to cart.', 'success')
            else:
                flash('Product not found.', 'error')
        else:
            flash('User not found. Please log in again.', 'error')
    else:
        flash('You need to log in to add items to your cart.', 'warning')
    
    return redirect(url_for('home'))

@app.route('/category/<string:category_id>')
def category(category_id):
    """ Displays products in a specific category """
    category = storage.get(Category, category_id)
    if category:
        products = [product for product in storage.all(Product).values() if product.category_id == category_id]
        return render_template('category.html', category=category, products=products)
    else:
        flash('Category not found.', 'error')
        return redirect(url_for('home'))


@app.route('/add_to_favorites/<string:product_id>', methods=['POST'])
def add_to_favorites(product_id):
    """ Add a product to favorites """
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            product = storage.get(Product, product_id)
            if product:
                # Check if the product is already in favorites
                favorite_item = next((item for item in storage.all(Favorite).values() if item.product_id == product_id and item.user_id == user.id), None)
                
                if favorite_item:
                    flash('Product already in favorites.', 'info')
                else:
                    # Add the product to favorites
                    new_favorite_item = Favorite(user_id=user.id, product_id=product_id)
                    storage.new(new_favorite_item)
                    storage.save()
                    flash('Product added to favorites.', 'success')
            else:
                flash('Product not found.', 'error')
        else:
            flash('User not found. Please log in again.', 'error')
    else:
        flash('You need to log in to add items to favorites.', 'warning')
    
    return redirect(url_for('home'))

@app.errorhandler(404)
def not_found_error(error):
    """ 404 Error handler """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """ 500 Error handler """
    return render_template('500.html'), 500

@app.route('/logout')
def logout():
    """ Log out the current user """
    session.pop('user_id', None)  # Remove the user_id from the session
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/remove_from_favorites/<string:product_id>')
def remove_from_favorites(product_id):
    """ Remove a product from favorites """
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            favorite_item = next((item for item in storage.all(Favorite).values() if item.product_id == product_id and item.user_id == user.id), None)
            if favorite_item:
                storage.delete(favorite_item)
                storage.save()
                flash('Product removed from favorites.', 'success')
            else:
                flash('Product not found in favorites.', 'error')
        else:
            flash('User not found. Please log in again.', 'error')
        return redirect(url_for('favorites'))
    else:
        flash('You need to log in to remove items from favorites.', 'warning')
        return redirect(url_for('login'))



if __name__ == "__main__":
    """ Main Function """ 
    app.run(host='0.0.0.0', port=5000, debug=True)
