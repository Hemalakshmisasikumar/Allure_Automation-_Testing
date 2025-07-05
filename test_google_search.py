import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.epic("Google Search Tests")
@allure.feature("Search Box")
class TestGoogleSearchBox:

    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.quit()

    @allure.title("Verify Google Search Box is Visible")
    @allure.description("Open Google homepage and verify the search box is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_box_visible(self):
        with allure.step("Navigate to Google homepage"):
            self.driver.get("https://www.google.com/")

        with allure.step("Wait for the search box to be visible"):
            wait = WebDriverWait(self.driver, 10)
            searchbox = wait.until(EC.visibility_of_element_located((By.NAME, "q")))

        with allure.step("Verify the search box is displayed"):
            assert searchbox.is_displayed(), "Search box should be displayed"

        with allure.step("Print confirmation"):
            print("Search box is visible on Google Chrome")
