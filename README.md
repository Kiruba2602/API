# Little Lemon API

Welcome to the Little Lemon API, your go-to virtual restaurant management system! Crafted with Django and Django Rest Framework, this RESTful API makes handling your restaurant's menu and categories a breeze. Whether you're adding new tantalizing dishes or organizing them into categories, Little Lemon API simplifies these processes with an intuitive interface.

## Getting Started

Follow these steps to get your Little Lemon API up and running.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python (3.7 or later)
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Kiruba2602/API/little-lemon-api.git
```

2. **Navigate to the project directory**

```bash
cd little-lemon-api
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Setup the database**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Start the server**

```bash
python manage.py runserver
```

The API will now be accessible at [http://localhost:8000](http://localhost:8000).

## Endpoints

The Little Lemon API offers a variety of endpoints for managing your menu items and categories.

### Menu Items

- **Get all menu items**: `GET /menu-items`
- **Get a single menu item**: `GET /menu-items/:id`
- **Create a new menu item**: `POST /menu-items`
- **Update a menu item**: `PUT /menu-items/:id`
- **Delete a menu item**: `DELETE /menu-items/:id`

### Menu Categories

- **Get all menu categories**: `GET /menu-categories`
- **Get a single menu category**: `GET /menu-categories/:id`
- **Create a new menu category**: `POST /menu-categories`
- **Update a menu category**: `PUT /menu-categories/:id`
- **Delete a menu category**: `DELETE /menu-categories/:id`

## Technologies Used

- Django & Django Rest Framework for the REST API
- SQLite for the database

## Contributing

We welcome contributions to the Little Lemon API! Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
