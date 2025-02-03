from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://ultimateqa.com/filling-out-forms')

# click categories drop down button
categories = driver.find_element(By.CSS_SELECTOR, '[id="menu-main-menu"] [id="menu-item-218225"]')
categories.click()

# wait for 4 sec
sleep(4)

free_courses_option = driver.find_element(By.CSS_SELECTOR, '[class="sub-menu"] [id="menu-item-217933"]')
actions = ActionChains(driver)
actions.move_to_element(free_courses_option)
actions.click()
actions.perform()

print('Test Passed')

driver.quit()
