import pytest
import allure
import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Login Test using CSV Data")
@allure.description("Reads login credentials from a CSV file and tests login functionality on DemoQA.")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_with_csv():
    csv_file = "data.csv"

    with allure.step("Check if CSV file exists"):
        if not os.path.exists(csv_file):
            allure.attach(f"{csv_file} not found", name="Missing CSV File", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"❌ CSV file '{csv_file}' not found in the project directory.")

    with allure.step("Launch browser and open login page"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demoqa.com/login")
        wait = WebDriverWait(driver, 10)

    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                username = row['username']
                password = row['password']

                with allure.step(f"Attempt login with username: {username}"):
                    # Enter username
                    user_input = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
                    driver.execute_script("arguments[0].scrollIntoView(true);", user_input)
                    ActionChains(driver).move_to_element(user_input).perform()
                    user_input.clear()
                    user_input.send_keys(username)

                    # Enter password
                    pass_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
                    driver.execute_script("arguments[0].scrollIntoView(true);", pass_input)
                    ActionChains(driver).move_to_element(pass_input).perform()
                    pass_input.clear()
                    pass_input.send_keys(password)

                    # Click login button
                    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
                    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
                    login_button.click()
                    time.sleep(2)

                    # Attach current URL for trace
                    current_url = driver.current_url
                    allure.attach(current_url, name=f"{username}_PostLoginURL", attachment_type=allure.attachment_type.TEXT)

                    # Navigate back for next login
                    driver.get("https://demoqa.com/login")
                    time.sleep(1)

    except Exception as e:
        allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise

    finally:
        with allure.step("Close browser"):
            driver.quit()
