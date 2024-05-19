import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from flask import Flask
from apps import db
from apps.models import AccountDimension
from werkzeug.security import generate_password_hash

class OnlyRecipesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.base_url = "http://127.0.0.1:5000" 

        # Setup Flask app context to access the database
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use a test database
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SECRET_KEY'] = 'supersecretkey'
        app.app_context().push()

        db.init_app(app)
        db.create_all()

        # Check if test user exists, if not, create it
        with app.app_context():
            testuser = AccountDimension.query.filter_by(username="test").first()
            if not testuser:
                hashed_password = generate_password_hash("admin")
                testuser = AccountDimension(username="test", email="test@gmail.com", password=hashed_password)
                db.session.add(testuser)
                db.session.commit()

    def login(self, username, password):
        self.driver.get(f"{self.base_url}/auth/login")
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
        sleep(2)  # Wait for login to complete and redirection

    def test_login_page(self):
        self.driver.get(f"{self.base_url}/auth/login")
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

        self.assertIsNotNone(username_input)
        self.assertIsNotNone(password_input)
        self.assertIsNotNone(submit_button)

        username_input.send_keys("test")
        password_input.send_keys("admin")
        submit_button.click()

        sleep(2)  # Wait for login to complete and redirection

    def test_account_page(self):
        self.login("test", "admin")  # Use the login method to authenticate
        self.driver.get(f"{self.base_url}/auth/account")
        sleep(2)  # Wait for the account page to load

        print("DEBUG: Page source after navigating to /auth/account")
        print(self.driver.page_source)  # Print the page source for debugging

        username_element = self.driver.find_element(By.ID, "username")
        self.assertIsNotNone(username_element, "Username element not found.")
        username = username_element.text
        print(f"DEBUG: username element text: '{username}'")
        self.assertEqual(username, "test", f"Expected username 'test', but got '{username}'")

        email_element = self.driver.find_element(By.ID, "email")
        self.assertIsNotNone(email_element, "Email element not found.")
        email = email_element.text
        print(f"DEBUG: email element text: '{email}'")
        self.assertEqual(email, "test@gmail.com", f"Expected email 'test@gmail.com', but got '{email}'")

    def test_popup_form(self):
        self.login("test", "admin")  # Use the login method to authenticate
        self.driver.get(f"{self.base_url}/auth/main")
        sleep(2)  # Wait for the main page to load

        print(self.driver.page_source)  # Print the page source for debugging

        try:
            open_form_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "request-btn"))
            )
            self.assertIsNotNone(open_form_button, "Popup form button not found.")
            open_form_button.click()
            sleep(1)
            form_title_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-form h2"))
            )
            self.assertIsNotNone(form_title_element, "Form title element not found.")
            form_title = form_title_element.text
            print(f"DEBUG: form title element text: '{form_title}'")
            self.assertEqual(form_title, "Request a Recipe", f"Expected form title 'Request a Recipe', but got '{form_title}'")
        except TimeoutException:
            print("DEBUG: request-btn not found within the specified time.")
            raise

    def test_recipe_cards(self):
        self.login("test", "admin")  # Use the login method to authenticate
        self.driver.get(f"{self.base_url}/auth/main")
        sleep(2)  # Wait for the main page to load

        print(self.driver.page_source)  # Print the page source for debugging

        cards = self.driver.find_elements(By.CLASS_NAME, "card")
        print(f"DEBUG: Number of recipe cards found: {len(cards)}")
        self.assertGreater(len(cards), 0)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
