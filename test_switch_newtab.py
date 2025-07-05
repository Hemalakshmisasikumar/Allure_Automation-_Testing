import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Browser Window Tests")
@allure.feature("Tab Navigation")
class TestBrowserWindows:

    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @allure.title("Test Navigation Between Tabs")
    @allure.description("Open a new tab and navigate back to the main window")
    @allure.severity(allure.severity_level.NORMAL)
    def test_tab_navigation(self):
        with allure.step("Open demo page"):
            self.driver.get("https://demoqa.com/browser-windows")
            allure.attach("Main Window Title", self.driver.title, allure.attachment_type.TEXT)

        main_window = self.driver.current_window_handle

        with allure.step("Click on the tab button"):
            tab_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "tabButton"))
            )
            tab_button.click()
            allure.attach("Clicked Tab Button", "Tab button clicked successfully", allure.attachment_type.TEXT)

        with allure.step("Wait for a new tab to open"):
            WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
            all_windows = self.driver.window_handles

        with allure.step("Switch to the new tab"):
            for handle in all_windows:
                if handle != main_window:
                    self.driver.switch_to.window(handle)
                    break
            allure.attach("New Tab Title", self.driver.title, allure.attachment_type.TEXT)
            print("New tab title:", self.driver.title)

        with allure.step("Close the new tab and switch back to the main window"):
            self.driver.close()
            self.driver.switch_to.window(main_window)
            allure.attach("Back to Main Window Title", self.driver.title, allure.attachment_type.TEXT)
            print("Back to main window:", self.driver.title)
