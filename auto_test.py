from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/upload")

# Locate the file input field
file_input = driver.find_element(By.ID, "file-upload")

# Upload your file
file_input.send_keys(r"C:\Users\VAIROCHANA\Desktop\ups.txt")

# Click the upload button
driver.find_element(By.ID, "file-submit").click()

# Wait to see the result
time.sleep(3)
driver.quit()
