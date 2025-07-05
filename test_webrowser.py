import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Google Search Tests")
@allure.feature("Search Box Visibility")
class TestGoogleSearchBox:

    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.quit()

    @allure.title("Test Search Box Visibility on Google")
    @allure.description("Verify that the search box is visible on the Google homepage")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_box_visible(self):
        with allure.step("Open Google homepage"):
            self.driver.get("https://www.google.com/")
            allure.attach("Page Title", self.driver.title, allure.attachment_type.TEXT)

        wait = WebDriverWait(self.driver, 10)
        
        with allure.step("Wait for the search box to be visible"):
            searchbox = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
            allure.attach("Search Box Visibility", str(searchbox.is_displayed()), allure.attachment_type.TEXT)

        with allure.step("Assert that the search box is displayed"):
            assert searchbox.is_displayed(), "Search box should be displayed"
            print("Search box is visible on Google Chrome")
