# OnlyRecipes

## Overview
OnlyRecipes is a web application designed as a recipe request forum. Users can create accounts, post and respond to recipe requests, and search for recipes with various filters for meal types.

## Features
- User Authentication (Login, Registration)
- Recipe Requests
- Recipe Responses
- Search Functionality
- Comments on Recipes
- User Account Management

## Technologies Used
- Frontend: HTML, CSS, Bootstrap, JavaScript (JQuery, AJAX)
- Backend: Flask, Websockets
- Database: SQLite with SQLAlchemy
- Testing: Selenium, Unittest

## Project Structure
```plaintext
├── apps
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   ├── form.py
│   ├── static
│   │   ├── css
│   │   ├── js
│   └── templates
│       ├── account.html
│       ├── cards.html
│       ├── login.html
│       ├── main.html
│       ├── register.html
│       └── popupForm.html
├── migrations
├── tests
│   ├── __init__.py
│   └── test_app.py
├── venv
├── .flaskenv
├── config.py
├── app.py
├── requirements.txt
└── README.md

**Setup**
Prerequisites
Python 3.10

## Installation
1. Clone the repository:
    git clone https://github.com/your-repo/onlyrecipes.git #UPDATE WITH LINK PLEASE
    cd onlyrecipes
2. Create and activate a virtual environment:
    python -m venv venv (or use 'python3 -m venv venv' on mac)
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required dependencies
    pip install -r requirements.txt
4. Setup the initial database
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade

## Running the Application
1. Start the flask server
    flask run
2. Open your web browser and go to http://127.0.0.1:5000 to access OnlyRecipes.

## Running Tests
1. Ensure the flask server is running
2. In a separate terminal, run the tests 
    python -m unittest discover -s tests

## Usage
User Authentication
- Login: Users can log in using their username and password.
- Registration: New users can create an account.

Recipe Requests
- Users can post new recipe requests specifying meal type, title, and ingredients.
- Users can respond to recipe requests with their recipes.

Searching Recipes
- Users can search for recipes by specifying meal type and ingredients.

Comments
- Users can comment on recipes and view comments left by others.

Account Management
- Users can view and manage their account details.
- Users can see a list of their recipe requests and update or delete them if necessary.

Contribution
- Feel free to fork this repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
MIT

Contact
For any questions, please contact [your-email@example.com].