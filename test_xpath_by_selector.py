import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Menu Redirection Test")
@allure.description("Verify that the 'Blog' and 'Contact' menu items redirect correctly on the Practice Test Automation website.")
@allure.severity(allure.severity_level.CRITICAL)
def test_menu_redirection():
    with allure.step("Initialize Chrome browser"):
        driver = webdriver.Chrome()
        driver.maximize_window()

    with allure.step("Open Practice Test Automation homepage"):
        driver.get("https://practicetestautomation.com/")
        time.sleep(2)

    menu_items = {
        "Blog": ("a[href*='blog']", "blog"),
        "Contact": ("a[href*='contact']", "contact")
    }

    for name, (css_selector, expected_url_part) in menu_items.items():
        with allure.step(f"Click on {name} link and verify redirection"):
            try:
                link = driver.find_element(By.CSS_SELECTOR, css_selector)
                link.click()
                time.sleep(2)

                current_url = driver.current_url
                allure.attach(current_url, name=f"{name} Page URL", attachment_type=allure.attachment_type.TEXT)

                assert expected_url_part in current_url, f"{name} does NOT redirect correctly"
                print(f"{name} redirects correctly ✅")

                # Navigate back to home for next item
                driver.get("https://practicetestautomation.com/")
                time.sleep(2)

            except Exception as e:
                allure.attach(str(e), name=f"{name} Exception", attachment_type=allure.attachment_type.TEXT)
                print(f"{name} redirection check failed ❌")
                raise

    with allure.step("Close browser"):
        driver.quit()
