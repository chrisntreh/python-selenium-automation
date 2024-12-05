from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# css
$$(".a-icon.a-icon-logo")
$$(".a-button-text")
$$(".a-input-text.a-span12.auth-autofocus   ")
driver.find_element(By.ID,"ap_email")
driver.find_element(By.ID,"ap_password")
driver.find_element(By.CSS_SELECTOR,"input.At. least. 6. characters")
driver.find_element(By.ID,"ap_password_check")
$$(".a-button-input")
$x("//a[contains(@href,'condition_of_use?')]")
$x("//a[contains(@href,'/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&amp;nodeId=468496>Privacy Notice</a>)']")
$$(".a-link-emphasis")


 @given('Open target main page')
# def open_main(context):
#     context.driver.get('https://www.target.com/')
#
#
# @when('click cart icon')
# def click_cart_icon(context):
#     context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
#     sleep(10)
#
#
# @then('verify empty sign is showing')
# def verify_empty_sign(context):
#     expected_results = 'Your cart is empty'
#     actual_results=context.driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 fJliSz']").text
#     assert expected_results == actual_results, f'Expected {expected_results}, but got {actual_results}'



@given('Open target main page')
def open_main(context):
 context.driver.get('https://www.target.com/')


@when('click sign in')
def click_sign_in(context):
     context.driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kkWqdY h-margin-r-x3']").click()


@then('verify sign in form is open')
def verify_sign_in_form(context):
    expected_results = 'Sign in to target account'
    actual_results=context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    assert expected_results == actual_results, f'Expected {expected_results}, but got {actual_results}'
    sleep(8)
