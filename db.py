from models import storage
from models.user import User
from models.category import Category
from models.product import Product

# Sample data for categories
categories = [
    {'name': 'Electronics', 'description': 'Devices and gadgets', 'image_url': 'static/images/electronics.jpg'},
    {'name': 'Clothing', 'description': 'Apparel and accessories', 'image_url': 'static/images/clothing.jpg'},
    {'name': 'Home & Kitchen', 'description': 'Furniture, appliances, and more', 'image_url': 'static/images/home_kitchen.jpg'},
    {'name': 'Sports', 'description': 'Sports equipment and apparel', 'image_url': 'static/images/sports.jpg'},
    {'name': 'Books', 'description': 'Various genres of books', 'image_url': 'static/images/books.jpg'},
    {'name': 'Toys', 'description': 'Fun and educational toys for all ages', 'image_url': 'static/images/toys.jpg'},
    {'name': 'Beauty', 'description': 'Cosmetics, skincare, and grooming products', 'image_url': 'static/images/beauty.jpg'},
    {'name': 'Automotive', 'description': 'Car parts and accessories', 'image_url': 'static/images/automotive.jpg'},
]

# Add categories to the database
for category_data in categories:
    category = Category(**category_data)
    storage.new(category)

storage.save()

# Retrieve category IDs from the database
category_ids = {cat.name: cat.id for cat in storage.all(Category).values()}

# Extended list of products
products = [
    {'name': 'Smartphone', 'price': 699, 'description': 'Latest model smartphone with high resolution display', 'quantity': 50, 'category_id': category_ids['Electronics'], 'image_url': 'static/images/smartphone.jpg'},
    {'name': 'Laptop', 'price': 999, 'description': 'High-performance laptop with fast processor', 'quantity': 30, 'category_id': category_ids['Electronics'], 'image_url': 'static/images/laptop.jpg'},
    {'name': 'T-Shirt', 'price': 19, 'description': 'Comfortable cotton t-shirt in various colors', 'quantity': 100, 'category_id': category_ids['Clothing'], 'image_url': 'static/images/tshirt.jpg'},
    {'name': 'Running Shoes', 'price': 89, 'description': 'Durable and comfortable running shoes', 'quantity': 70, 'category_id': category_ids['Clothing'], 'image_url': 'static/images/running_shoes.jpg'},
    {'name': 'Coffee Maker', 'price': 120, 'description': 'Automatic coffee maker with programmable settings', 'quantity': 40, 'category_id': category_ids['Home & Kitchen'], 'image_url': 'static/images/coffee_maker.jpg'},
    {'name': 'Blender', 'price': 60, 'description': 'Powerful blender for smoothies and more', 'quantity': 60, 'category_id': category_ids['Home & Kitchen'], 'image_url': 'static/images/blender.jpg'},
    {'name': 'Yoga Mat', 'price': 25, 'description': 'Non-slip yoga mat for your workout sessions', 'quantity': 90, 'category_id': category_ids['Sports'], 'image_url': 'static/images/yoga_mat.jpg'},
    {'name': 'Basketball', 'price': 30, 'description': 'Official size basketball for outdoor play', 'quantity': 50, 'category_id': category_ids['Sports'], 'image_url': 'static/images/basketball.jpg'},
    {'name': 'The Great Gatsby', 'price': 15, 'description': 'Classic novel by F. Scott Fitzgerald', 'quantity': 200, 'category_id': category_ids['Books'], 'image_url': 'static/images/great_gatsby.jpg'},
    {'name': '1984', 'price': 18, 'description': 'Dystopian novel by George Orwell', 'quantity': 180, 'category_id': category_ids['Books'], 'image_url': 'static/images/1984.jpg'},
    {'name': 'Building Blocks Set', 'price': 45, 'description': 'Creative building blocks for kids', 'quantity': 150, 'category_id': category_ids['Toys'], 'image_url': 'static/images/building_blocks.jpg'},
    {'name': 'Dollhouse', 'price': 150, 'description': 'Wooden dollhouse with furniture', 'quantity': 40, 'category_id': category_ids['Toys'], 'image_url': 'static/images/dollhouse.jpg'},
    {'name': 'Moisturizer', 'price': 25, 'description': 'Hydrating moisturizer for all skin types', 'quantity': 100, 'category_id': category_ids['Beauty'], 'image_url': 'static/images/moisturizer.jpg'},
    {'name': 'Shampoo', 'price': 15, 'description': 'Gentle shampoo for everyday use', 'quantity': 120, 'category_id': category_ids['Beauty'], 'image_url': 'static/images/shampoo.jpg'},
    {'name': 'Car Battery', 'price': 120, 'description': 'Reliable car battery for most vehicles', 'quantity': 60, 'category_id': category_ids['Automotive'], 'image_url': 'static/images/car_battery.jpg'},
    {'name': 'Motor Oil', 'price': 30, 'description': 'High-quality motor oil for smooth engine performance', 'quantity': 80, 'category_id': category_ids['Automotive'], 'image_url': 'static/images/motor_oil.jpg'},
    # Additional products
    {'name': 'Smart Watch', 'price': 199, 'description': 'Stylish smartwatch with health tracking features', 'quantity': 40, 'category_id': category_ids['Electronics'], 'image_url': 'static/images/smart_watch.jpg'},
    {'name': 'Tablet', 'price': 299, 'description': 'High-resolution tablet with a sleek design', 'quantity': 25, 'category_id': category_ids['Electronics'], 'image_url': 'static/images/tablet.jpg'},
    {'name': 'Jacket', 'price': 89, 'description': 'Warm and stylish winter jacket', 'quantity': 60, 'category_id': category_ids['Clothing'], 'image_url': 'static/images/jacket.jpg'},
    {'name': 'Sunglasses', 'price': 45, 'description': 'Fashionable sunglasses with UV protection', 'quantity': 80, 'category_id': category_ids['Clothing'], 'image_url': 'static/images/sunglasses.jpg'},
    {'name': 'Microwave Oven', 'price': 150, 'description': 'Compact microwave oven with multiple settings', 'quantity': 35, 'category_id': category_ids['Home & Kitchen'], 'image_url': 'static/images/microwave_oven.jpg'},
    {'name': 'Toaster', 'price': 40, 'description': 'Four-slice toaster with adjustable browning control', 'quantity': 55, 'category_id': category_ids['Home & Kitchen'], 'image_url': 'static/images/toaster.jpg'},
    {'name': 'Tent', 'price': 120, 'description': 'Spacious camping tent with easy setup', 'quantity': 20, 'category_id': category_ids['Sports'], 'image_url': 'static/images/tent.jpg'},
    {'name': 'Sleeping Bag', 'price': 60, 'description': 'Comfortable sleeping bag for camping trips', 'quantity': 30, 'category_id': category_ids['Sports'], 'image_url': 'static/images/sleeping_bag.jpg'},
    {'name': 'Cookbook', 'price': 25, 'description': 'Collection of recipes for various cuisines', 'quantity': 100, 'category_id': category_ids['Books'], 'image_url': 'static/images/cookbook.jpg'},
    {'name': 'Puzzle Set', 'price': 35, 'description': 'Challenging puzzles for all ages', 'quantity': 70, 'category_id': category_ids['Toys'], 'image_url': 'static/images/puzzle_set.jpg'},
    {'name': 'Face Cream', 'price': 40, 'description': 'Nourishing face cream for all skin types', 'quantity': 90, 'category_id': category_ids['Beauty'], 'image_url': 'static/images/face_cream.jpg'},
    {'name': 'Hair Dryer', 'price': 60, 'description': 'High-performance hair dryer with multiple settings', 'quantity': 45, 'category_id': category_ids['Beauty'], 'image_url': 'static/images/hair_dryer.jpg'},
    {'name': 'Car Seat Cover', 'price': 35, 'description': 'Protective car seat cover with universal fit', 'quantity': 55, 'category_id': category_ids['Automotive'], 'image_url': 'static/images/car_seat_cover.jpg'},
    {'name': 'Car Vacuum Cleaner', 'price': 75, 'description': 'Portable vacuum cleaner for cars', 'quantity': 40, 'category_id': category_ids['Automotive'], 'image_url': 'static/images/car_vacuum_cleaner.jpg'},
]

# Add products to the database
for product_data in products:
    product = Product(**product_data)
    storage.new(product)

storage.save()

# Sample data for users
users = [
    {'email': 'john.doe@example.com', 'password': 'hashed_password', 'username': 'johndoe', 'first_name': 'John', 'last_name': 'Doe', 'phone_number': '123-456-7890', 'country': 'USA', 'city': 'New York', 'address': '123 Elm Street', 'postal_code': '10001'},
    {'email': 'jane.doe@example.com', 'password': 'hashed_password', 'username': 'janedoe', 'first_name': 'Jane', 'last_name': 'Doe', 'phone_number': '987-654-3210', 'country': 'USA', 'city': 'Los Angeles', 'address': '456 Oak Street', 'postal_code': '90001'},
    {'email': 'alice.smith@example.com', 'password': 'hashed_password', 'username': 'alicesmith', 'first_name': 'Alice', 'last_name': 'Smith', 'phone_number': '555-123-4567', 'country': 'USA', 'city': 'Chicago', 'address': '789 Maple Avenue', 'postal_code': '60601'},
    {'email': 'bob.jones@example.com', 'password': 'hashed_password', 'username': 'bobjones', 'first_name': 'Bob', 'last_name': 'Jones', 'phone_number': '555-987-6543', 'country': 'USA', 'city': 'San Francisco', 'address': '101 Pine Street', 'postal_code': '94101'},
    {'email': 'carol.white@example.com', 'password': 'hashed_password', 'username': 'carolwhite', 'first_name': 'Carol', 'last_name': 'White', 'phone_number': '555-234-5678', 'country': 'USA', 'city': 'Seattle', 'address': '202 Birch Road', 'postal_code': '98101'},
    {'email': 'dan.black@example.com', 'password': 'hashed_password', 'username': 'danblack', 'first_name': 'Dan', 'last_name': 'Black', 'phone_number': '555-876-5432', 'country': 'USA', 'city': 'Austin', 'address': '303 Cedar Street', 'postal_code': '73301'},
    {'email': 'emma.green@example.com', 'password': 'hashed_password', 'username': 'emmagreen', 'first_name': 'Emma', 'last_name': 'Green', 'phone_number': '555-345-6789', 'country': 'USA', 'city': 'Boston', 'address': '404 Elm Street', 'postal_code': '02101'},
    {'email': 'frank.kim@example.com', 'password': 'hashed_password', 'username': 'frankkim', 'first_name': 'Frank', 'last_name': 'Kim', 'phone_number': '555-654-3210', 'country': 'USA', 'city': 'Miami', 'address': '505 Oak Avenue', 'postal_code': '33101'},
]

# Add users to the database
for user_data in users:
    user = User(**user_data)
    storage.new(user)

storage.save()

print("Database populated with sample data.")
