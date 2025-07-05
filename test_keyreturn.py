import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Search Feature")
class TestSearch:

    @pytest.fixture(scope="class")
    def setup(self):
        driver = webdriver.Chrome()  # Ensure you have the ChromeDriver in your PATH
        driver.get("http://example.com")  # Replace with the actual URL
        yield driver  # Yield the driver so it can be used in tests
        driver.quit()  # Cleanup after tests

    @allure.story("Search for PyCon")
    def test_search_pycon(self, setup):
        driver = setup  # Use the driver passed from the fixture
        
        # Wait for the search box to be present
        try:
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))  # Adjust the selector as needed
            )
            search_box.send_keys("pycon")
            search_box.submit()

            # Check if results are found
            with allure.step("Check search results"):
                if "No results found." not in driver.page_source:
                    allure.attach("Search Result Status", "Searched results for 'pycon' found.", allure.attachment_type.TEXT)
                    print("Searched results for 'pycon' found.")
                else:
                    allure.attach("Search Result Status", "'pycon' does not exist in search results.", allure.attachment_type.TEXT)
                    print("'pycon' does not exist in search results.")
        except Exception as e:
            allure.attach("Error", str(e), allure.attachment_type.TEXT)
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    pytest.main()
