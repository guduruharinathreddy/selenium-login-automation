from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_test(username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)

    message = driver.find_element(By.ID, "flash").text

    if "You logged into a secure area!" in message:
        print("Login Test Passed ✅")
    else:
        print("Login Test Failed ❌")

    driver.quit()


# Call function
login_test("tomsmith", "SuperSecretPassword!")