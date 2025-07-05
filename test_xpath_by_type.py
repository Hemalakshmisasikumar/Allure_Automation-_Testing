import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Practice Form Input Test")
@allure.description("Fills out the first name, last name, and email fields on the DemoQA practice form.")
@allure.severity(allure.severity_level.NORMAL)
def test_practice_form_input():
    with allure.step("Launch browser and open the practice form page"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demoqa.com/automation-practice-form")
        time.sleep(2)

    try:
        with allure.step("Enter First Name"):
            first_name = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
            first_name.clear()
            first_name.send_keys("sneha")
            allure.attach("sneha", name="First Name Entered", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Enter Last Name"):
            last_name = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
            last_name.clear()
            last_name.send_keys("latha")
            allure.attach("latha", name="Last Name Entered", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Enter Email"):
            email = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
            email.clear()
            email.send_keys("sneha@gmail.com")
            allure.attach("sneha@gmail.com", name="Email Entered", attachment_type=allure.attachment_type.TEXT)

    except Exception as e:
        allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise

    finally:
        with allure.step("Close browser"):
            time.sleep(3)
            driver.quit()
