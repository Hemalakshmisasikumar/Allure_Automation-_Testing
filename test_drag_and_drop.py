import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@allure.title("Drag and Drop Test")
@allure.description("Test to verify drag-and-drop functionality on jQuery UI demo page.")
@allure.severity(allure.severity_level.CRITICAL)
def test_drag_and_drop():
    with allure.step("Launch browser and open URL"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/droppable/")

    try:
        with allure.step("Switch to iframe containing draggable elements"):
            iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
            driver.switch_to.frame(iframe)

        with allure.step("Locate draggable and droppable elements"):
            source = driver.find_element(By.ID, "draggable")
            target = driver.find_element(By.ID, "droppable")

        with allure.step("Perform drag and drop action"):
            actions = ActionChains(driver)
            actions.drag_and_drop(source, target).perform()
            time.sleep(2)  # wait for the text to change

        with allure.step("Validate the result of drag and drop"):
            assert target.text.strip() == "Dropped!", "Drag and drop not successful"
            allure.attach(target.text, name="Target Text", attachment_type=allure.attachment_type.TEXT)

    finally:
        with allure.step("Close browser"):
            driver.switch_to.default_content()
            driver.quit()
