from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target help page')
def open_target_help(context):
    context.driver.get('https://help.target.com/help')
    sleep(5)


@then('Verify these UI elements are present')
def verify_ui_elements(context):
    context.driver.find_element(By.CSS_SELECTOR, '[class="section header-section"]')
    sleep(8)




@when('Verify these UI elements are present')
def verify_ui_elements(context):
    context.driver.find_element(By.XPATH, "//h2[@class='custom-h2']")
    context.driver.find_element(By.XPATH, "//div[@class='form-search form-inline']")
    context.driver.find_element(By.XPATH, "//div[@class='col-lg-12']")
    context.driver.find_element(By.XPATH, "//div[@class='container clearfix']")
    context.driver.find_element(By.XPATH, "//div[@class='home-container']")


#@then('verify access to the help page')
#def verify_access_help(context):
#    expected_results = 'verify access to the help page'
#    actual_results=context.driver.find_element(By.XPATH, "//section[@class='section header-section']")
#    assert expected_results == actual_results, f'Expected {expected_results}, but got {actual_results}'
#    sleep(8)