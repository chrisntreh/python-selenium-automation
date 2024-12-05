from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @given('Open target main page')
# def open_main(context):
#     context.driver.get('https://www.target.com/')

# @when('Search for tea')
# def search_product(context):
#     context.driver.find_element(By.ID, 'search').send_keys('tea')
#     context.driver.find_element(By.XPATH,'//button[@data-test=@web/Search/SearchInput').click()
#
#
# @then('verify search results shown')
# def verify_search_results(context):
#     expected_results = 'tea'
#     actual_results = context.driver.find_element(By.XPATH,"//div[@data-test='resultsHanding']").text
#############################################


# @given('Open target main page')
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
