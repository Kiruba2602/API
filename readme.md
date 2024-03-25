Little Lemon API
Welcome to the Little Lemon API! This is a RESTful API built with Node.js and Express that allows you to manage a virtual restaurant's menu.

Getting Started
To get started with the Little Lemon API, follow these steps:

Clone the repository:
git clone https://github.com/yourusername/little-lemon-api.git

Install the dependencies:
pip install requirements.txt

Start the server:
Run python manage.py makemigrations
Run python manage.py migrate
Run python manage.py runserver
The API will be running on http://localhost:3000.

Endpoints
Menu Items
Get all menu items: GET /menu-items
Get a single menu item: GET /menu-items/:id
Create a new menu item: POST /menu-items
Update a menu item: PUT /menu-items/:id
Delete a menu item: DELETE /menu-items/:id
Menu Categories
Get all menu categories: GET /menu-categories
Get a single menu category: GET /menu-categories/:id
Create a new menu category: POST /menu-categories
Update a menu category: PUT /menu-categories/:id
Delete a menu category: DELETE /menu-categories/:id
Technologies Used
DjangoRestFramework
REST API
db.SQLite
