import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from datetime import datetime

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.ID, "submit")

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
        return self.driver.find_element(*self.message_header).text

@allure.title("Login Test with Screenshot")
@allure.description("Test login functionality on practice-test-login page with screenshot capture")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_valid_user():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.implicitly_wait(5)

    login_page = LoginPage(driver)
    secure_area = SecureAreaPage(driver)

    try:
        login_page.enter_username("student")
        login_page.enter_password("Password123")

        # Create screenshots folder if not exists
        os.makedirs("screenshots", exist_ok=True)

        # Save screenshot before clicking submit
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshots/screenshot_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="Login Page Screenshot", attachment_type=allure.attachment_type.PNG)

        login_page.click_submit()

        msg = secure_area.get_message()
        allure.attach(msg, name="Login Message", attachment_type=allure.attachment_type.TEXT)

        assert "Logged In Successfully" in msg, "Login failed or message not found"

    finally:
        driver.quit()
