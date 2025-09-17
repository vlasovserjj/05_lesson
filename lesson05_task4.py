from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

sleep(1)

user_locator = "#username"

user_name = driver.find_element(By.CSS_SELECTOR, user_locator)
user_name.send_keys("tomsmith")

sleep(1)

password_locator = "#password"

password = driver.find_element(By.CSS_SELECTOR, password_locator)
password.send_keys("SuperSecretPassword!")
sleep(1)

click_locator = "i.fa.fa-2x"
click_login = driver.find_element(By.CSS_SELECTOR, click_locator)
click_login.click()

sleep(1)

messege = "div.flash"
green_text = driver.find_element(By.CSS_SELECTOR, messege).text

print(green_text)
driver.quit()
