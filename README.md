# AWD-Project: OnlyRecipes Read-Me
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
├── config.py
├── app.py
├── requirements.txt
└── README.md
```

# Setup
The following is just a basic outline of how to get the website up and running. For the most up-to-date information please check the release notes.

## Prerequisites
1. alembic (1.13.1+)
2. blinker (1.8.1+)
3. click (8.1.7+)
4. dnspython (2.6.1+)
5. email_validator (2.1.1+)
6. Flask (3.0.3+)
7. Flask-Login (0.6.3+)
8. Flask-Migrate (4.0.7+)
9. Flask-SQLAlchemy (3.1.1+)
10. Flask-WTF (1.2.1+)
11. greenlet (3.0.3+)
12. idna (3.7+)
13. itsdangerous (2.2.0+)
14. Jinja2 (3.1.3+)
15. Mako (1.3.3+)
16. MarkupSafe (2.1.5+)
17. python-dotenv (1.0.1+)
18. SQLAlchemy (2.0.29+)
19. typing_extensions (4.11.0+)
20. Werkzeug (3.0.2+)
21. WTForms (3.1.2+)


## Installation
1. Clone the repository:
    - git clone https://github.com/JeremyB2000/AWD-Project.git
    - cd onlyrecipes
3. Create and activate a virtual environment:
    - python -m venv venv (or use 'python3 -m venv venv' on mac)
    - source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4. Install the required dependencies
    - pip install -r requirements.txt
5. Setup the initial database
    - flask db init
    - flask db migrate -m "Initial migration."
    - flask db upgrade

## Running the Application
1. Start the flask server
    - flask run
2. Open your web browser and go to http://127.0.0.1:5000 to access OnlyRecipes.

## Running Tests
1. Ensure the flask server is running
2. In a separate terminal, run the tests 
    python -m unittest discover -s tests

## Usage

**User Authentication**
- Login: Users can log in using their username and password.
- Registration: New users can create an account.

**Recipe Requests**
- Users can post new recipe requests specifying meal type, title, and ingredients.
- Users can respond to recipe requests with their recipes.

**Searching Recipes**
- Users can search for recipes by specifying meal type and ingredients.

**Comments**
- Users can comment on recipes and view comments left by others.

**Account Management**
- Users can view and manage their account details.
- Users can see a list of their recipe requests and update or delete them if necessary.

**Contribution**
- Feel free to fork this repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Troubleshooting
1. Database Issues:
    If you encounter issues with the database, try resetting it with:
- flask db downgrade
- flask db upgrade
2. Selenium Errors:
- Ensure that ChromeDriver is installed and is compatible with your installed version of Chrome.
- Verify that the elements being accessed in the tests have the correct IDs or class names.
- General Errors: Check the Flask server logs for detailed error messages and stack traces.
3. Missing Dependencies:
- Please nsure all required packages are installed by running:
- pip install -r requirements.txt

## License
MIT
