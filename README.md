# E-commerce Flask Application

An e-commerce web application built with Flask, designed to allow users to browse and purchase products. The app includes features for managing user profiles, product categories, carts, favorites, and admin functionalities like product management and uploading images.

## Features

- **User Authentication**: Users can register, log in, and manage their profiles, including uploading profile pictures.
- **Product Management**: Admins can add, edit, and delete products. The app supports uploading product images.
- **Cart Management**: Users can add items to their shopping cart, view the cart, and remove items as needed.
- **Favorites**: Users can add products to their favorites list for easy access later.
- **Category Browsing**: Products can be viewed and filtered by categories for easier navigation.
- **Admin Panel**: Administrators have access to tools for managing products, categories, users, and image uploads.
- **Responsive Design**: The front end is styled with Bootstrap 5, ensuring a modern and mobile-friendly interface.

## Project Structure

```bash
.
├── main.py
├── models/
│   ├── base_model.py
│   ├── cart.py
│   ├── category.py
│   ├── product.py
│   ├── user.py
│   └── ...
├── web_flask/
│   ├── app.py
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── uploads/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── ...
│   └── ...
└── setup_db.sh

```

## Project Structure

- **Python 3.x**
- **Flask**
- **Bootstrap 5 (included via CDN)***
- **SQLite*** (or any database supported by SQLAlchemy)

## Usage

- **Register**: Create a user account to browse products, add items to your cart, and save favorite products.
- **Admin Features**: Log in as an admin to manage products, categories, and users. Upload and manage product images.
- **Cart Management**: Add items to the cart, update quantities, and remove items when necessary.
- **Favorites**: Save products to your favorites list for future reference.

## Screenshots:
