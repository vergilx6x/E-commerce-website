from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from models import storage
from models.product import Product
from models.user import User
from models.cart import Cart
from models.cart_item import Cart_item
from models.favorite import Favorite
from models.category import Category
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

UPLOAD_FOLDER = os.path.join('web_flask', 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.teardown_appcontext
def close_db(error):
    storage.close()

@app.route('/home', strict_slashes=False)
def home():
    # Fetch all categories
    categories = storage.all(Category).values()
    
    # Fetch all products
    all_products = list(storage.all(Product).values())
    
    # Sort products by creation date in descending order
    all_products.sort(key=lambda p: p.created_at, reverse=True)
    
    # Get the 10 most recent products
    new_products = all_products[:10]
    
    return render_template('home.html', categories=categories, all_products=all_products, new_products=new_products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        image = request.files.get('image')
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        image_url = save_image(image) if image else None
        new_user = User(email=email, password=hashed_password, username=username, image_url=image_url)
        
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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = storage.get_user(username)
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and/or password.', 'error')
    
    return render_template('login.html')


@app.route('/cart')
def cart():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            cart_items = storage.all(Cart_item).values()
            user_cart_items = []
            for item in cart_items:
                cart = storage.get(Cart, item.cart_id)
                if cart is not None and cart.user_id == user.id:
                    user_cart_items.append(item)
                elif cart is None:
                    print(f"Warning: Cart with ID {item.cart_id} not found.")
            return render_template('cart.html', cart_items=user_cart_items)
        else:
            flash('User not found. Please log in again.', 'error')
            return redirect(url_for('login'))
    else:
        flash('You need to log in to access the cart.', 'warning')
        return redirect(url_for('login'))


@app.route('/favorites')
def favorites():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        favorite_items = storage.all(Favorite).values()
        user_favorites = [item for item in favorite_items if item.user_id == user.id]
        return render_template('favorites.html', favorite_items=user_favorites)
    else:
        flash('You need to log in to access favorites.', 'warning')
        return redirect(url_for('login'))

@app.route('/user_profile')
def user_profile():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        return render_template('user_profile.html', user=user)
    else:
        flash('You need to log in to access your profile.', 'warning')
        return redirect(url_for('login'))

@app.route('/remove_from_cart/<string:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            cart_item = next((item for item in storage.all(Cart_item).values() if item.product_id == product_id and storage.get(Cart, item.cart_id).user_id == user.id), None)
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
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            product = storage.get(Product, product_id)
            if product:
                user_cart = next((cart for cart in storage.all(Cart).values() if cart.user_id == user.id), None)
                
                if not user_cart:
                    user_cart = Cart(user_id=user.id)
                    storage.new(user_cart)
                    storage.save()

                existing_item = next((item for item in storage.all(Cart_item).values() if item.product_id == product_id and item.cart_id == user_cart.id), None)
                
                if existing_item:
                    flash('Product already in cart.', 'info')
                else:
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
    
    return redirect(url_for('cart'))

@app.route('/category/<string:category_id>')
def category(category_id):
    category = storage.get(Category, category_id)
    if category:
        products = [product for product in storage.all(Product).values() if product.category_id == category_id]
        return render_template('category.html', category=category, products=products)
    else:
        flash('Category not found.', 'error')
        return redirect(url_for('home'))

@app.route('/add_to_favorites/<string:product_id>', methods=['POST'])
def add_to_favorites(product_id):
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if user:
            product = storage.get(Product, product_id)
            if product:
                favorite_item = next((item for item in storage.all(Favorite).values() if item.product_id == product_id and item.user_id == user.id), None)
                
                if favorite_item:
                    flash('Product already in favorites.', 'info')
                else:
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

@app.route('/remove_from_favorites/<string:product_id>', methods=['POST'])
def remove_from_favorites(product_id):
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

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/admin', methods=['GET'])
def admin_dashboard():
    users = storage.all(User).values()
    products = storage.all(Product).values()
    return render_template('admin_dashboard.html', users=users, products=products)

@app.route('/admin/users', methods=['GET', 'POST'])
def admin_users():
    if request.method == 'POST':
        action = request.form.get('action')
        user_id = request.form.get('user_id')

        if action == 'delete' and user_id:
            user = storage.get(User, user_id)
            if user:
                storage.delete(user)
                storage.save()
                flash('User deleted successfully.', 'success')
            else:
                flash('User not found.', 'error')

        elif action == 'edit' and user_id:
            email = request.form.get('email')
            username = request.form.get('username')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            phone_number = request.form.get('phone_number')
            country = request.form.get('country')
            city = request.form.get('city')
            address = request.form.get('address')
            postal_code = request.form.get('postal_code')
            image = request.files.get('image')

            user = storage.get(User, user_id)
            if user:
                user.email = email
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.phone_number = phone_number
                user.country = country
                user.city = city
                user.address = address
                user.postal_code = postal_code

                if image:
                    user.image_url = save_image(image)
                
                storage.save()
                flash('User updated successfully.', 'success')
            else:
                flash('User not found.', 'error')

        elif action == 'add':
            email = request.form.get('email')
            username = request.form.get('username')
            password = request.form.get('password')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            phone_number = request.form.get('phone_number')
            country = request.form.get('country')
            city = request.form.get('city')
            address = request.form.get('address')
            postal_code = request.form.get('postal_code')
            image = request.files.get('image')

            if storage.get(User, email=email):
                flash('User with this email already exists.', 'error')
            else:
                new_user = User(
                    email=email,
                    username=username,
                    password=password,  # You should hash the password before storing it
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone_number,
                    country=country,
                    city=city,
                    address=address,
                    postal_code=postal_code
                )
                if image:
                    new_user.image_url = save_image(image)
                
                storage.new(new_user)
                storage.save()
                flash('User added successfully.', 'success')

    users = storage.all(User).values()
    return render_template('admin_users.html', users=users)

@app.route('/admin/products', methods=['GET', 'POST'])
def admin_products():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        action = request.form.get('action')

        # Handle Delete Action
        if action == 'delete' and product_id:
            product = storage.get(Product, product_id)
            if product:
                storage.delete(product)
                storage.save()
                flash('Product deleted successfully.', 'success')
            else:
                flash('Product not found.', 'error')

        # Handle Edit Action
        if action == 'edit' and product_id:
            name = request.form.get('name')
            price = request.form.get('price')
            description = request.form.get('description')
            quantity = request.form.get('quantity')
            category_id = request.form.get('category_id')
            image = request.files.get('image')
            product = storage.get(Product, product_id)
            if product:
                product.name = name
                product.price = price
                product.description = description
                product.quantity = quantity
                product.category_id = category_id
                if image:
                    product.image_url = save_image(image)
                storage.save()
                flash('Product updated successfully.', 'success')
            else:
                flash('Product not found.', 'error')

        # Handle Add Product Action
        if action == 'add':
            name = request.form.get('name')
            price = request.form.get('price')
            description = request.form.get('description')
            quantity = request.form.get('quantity')
            category_id = request.form.get('category_id')
            image = request.files.get('image')
            new_product = Product(
                name=name,
                price=price,
                description=description,
                quantity=quantity,
                category_id=category_id
            )
            if image:
                new_product.image_url = save_image(image)
            storage.new(new_product)
            storage.save()
            flash('Product added successfully.', 'success')

    products = storage.all(Product).values()
    categories = storage.all(Category).values()
    return render_template('admin_products.html', products=products, categories=categories)


@app.route('/admin/upload_product_image/<string:product_id>', methods=['GET', 'POST'])
def upload_product_image(product_id):
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            product = storage.get(Product, product_id)
            if product:
                # Use the product's name for the image file
                image_url = save_image(file, product_id)
                product.image_url = image_url
                storage.save()
                flash('Image successfully uploaded and associated with product.', 'success')
            else:
                flash('Product not found.', 'error')
            return redirect(url_for('admin_products'))

    return render_template('admin_upload_product_image.html', product_id=product_id)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if 'user_id' in session:
        user = storage.get(User, session['user_id'])
        if request.method == 'POST':
            user.email = request.form.get('email')
            user.username = request.form.get('username')
            image = request.files.get('image')
            if image:
                user.image_url = save_image(image, user.id)
            storage.save()
            flash('Profile updated successfully.', 'success')
            return redirect(url_for('user_profile'))
        return render_template('edit_profile.html', user=user)
    else:
        flash('You need to log in to edit your profile.', 'warning')
        return redirect(url_for('login'))

def save_image(file, identifier=None):
    if file and allowed_file(file.filename):
        # Sanitize the identifier to ensure it's a valid filename
        sanitized_name = secure_filename(identifier) if identifier else secure_filename(file.filename)
        # Extract the file extension from the uploaded file
        file_extension = os.path.splitext(file.filename)[1].lower()
        # Construct the filename with the proper extension
        filename = f"{sanitized_name}{file_extension}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # Return the URL to access the image
        return url_for('static', filename='uploads/' + filename)
    return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
