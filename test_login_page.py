import os
import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        with allure.step("Enter username"):
            username = self.driver.find_element(By.ID, "username")
            username.send_keys("student")

        with allure.step("Enter password"):
            password = self.driver.find_element(By.ID, "password")
            password.send_keys("Password123")

        with allure.step("Submit the login form"):
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()

        # Wait for the message to appear
        time.sleep(2)  # You can replace this with an explicit wait if needed

        with allure.step("Check login success message"):
            msg = self.driver.find_element(By.TAG_NAME, 'h1').text
            if "Logged In Successfully" in msg:
                print("Login successful")
                allure.attach("Login Message", msg, allure.attachment_type.TEXT)
                assert True
            else:
                print("Login Failed")
                allure.attach("Login Message", msg, allure.attachment_type.TEXT)
                assert False

