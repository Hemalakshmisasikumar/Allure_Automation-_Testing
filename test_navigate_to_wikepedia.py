import pytest
import allure
from selenium import webdriver
import time


@allure.epic("Browser Navigation Tests")
@allure.feature("Navigation")
class TestBrowserNavigation:

    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @allure.title("Test Google to Wikipedia Navigation")
    @allure.description("Navigate from Google to Wikipedia and back")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigation(self):
        with allure.step("Open Google"):
            self.driver.get("https://www.google.com")
            allure.attach("Google Page Title", self.driver.title, allure.attachment_type.TEXT)
            print("Opened:", self.driver.title)
            time.sleep(2)

        with allure.step("Open Wikipedia"):
            self.driver.get("https://www.wikipedia.org")
            allure.attach("Wikipedia Page Title", self.driver.title, allure.attachment_type.TEXT)
            print("Opened:", self.driver.title)
            time.sleep(2)

        with allure.step("Navigate Back to Google"):
            self.driver.back()
            allure.attach("Back to Page Title", self.driver.title, allure.attachment_type.TEXT)
            print("Back to:", self.driver.title)
            time.sleep(2)

        with allure.step("Navigate Forward to Wikipedia"):
            self.driver.forward()
            allure.attach("Forward to Page Title", self.driver.title, allure.attachment_type.TEXT)
            print("Forward to:", self.driver.title)
            time.sleep(2)

        with allure.step("Refresh Wikipedia Page"):
            self.driver.refresh()
            allure.attach("Page Refreshed Title", self.driver.title, allure.attachment_type.TEXT)
            print("Page refreshed:", self.driver.title)
            time.sleep(2)

        with allure.step("Print Current URL"):
            current_url = self.driver.current_url
            print("Current URL:", current_url)
            allure.attach("Current URL", current_url, allure.attachment_type.TEXT)
