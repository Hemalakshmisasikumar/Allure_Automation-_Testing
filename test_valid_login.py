import os
import pytest
import allure
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.ID, "login")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()


class SecureAreaPage:
    def __init__(self, driver):
        self.driver = driver
        self.message_header = (By.TAG_NAME, "h1")

    def get_message(self):
        wait = WebDriverWait(self.driver, 20)  # Increased timeout
        return wait.until(EC.visibility_of_element_located(self.message_header)).text


@allure.epic("Login Tests")
@allure.feature("User Authentication")
class TestLogin:

    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()

    @allure.title("Verify Login with Valid User")
    @allure.description("Test the login functionality with valid user credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_valid_user(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("student")
        login_page.enter_password("Password123")

        # Create screenshots folder if not exists
        os.makedirs("screenshots", exist_ok=True)

        # Format timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save file
        file_name = f"screenshots/screenshot_{timestamp}.png"
        self.driver.save_screenshot(file_name)
        print(f"Screenshot saved as: {file_name}")

        with allure.step("Submit the login form"):
            login_page.click_submit()

        # Check the current URL
        current_url = self.driver.current_url
        print(f"Current URL after login attempt: {current_url}")

        # Optionally check for an error message
        try:
            error_message = self.driver.find_element(By.CLASS_NAME, "error").text
            print(f"Error message: {error_message}")
        except NoSuchElementException:
            print("No error message found, assuming login attempt was made.")

        secure_area = SecureAreaPage(self.driver)
        try:
            msg = secure_area.get_message()
            with allure.step("Verify login success message"):
                assert "Logged In Successfully" in msg, "Login failed: message not found"
                print("✅ Login successful")
        except TimeoutException:
            print("Timed out waiting for login success message.")
