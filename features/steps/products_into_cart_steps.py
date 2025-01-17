from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')


@given('Search for tea')
def search_product(context):
    #sleep(3)
    context.app.header.search_product()
    #context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()
    #sleep(3)

@when('Add to cart')
def add_to_cart(context):
    sleep(10)
    context.app.search_results.add_to_cart()


@when('access cart')
def access_cart(context):
    context.app.search_results.view_cart_cart_check_out()




@then('verify 1 item is added to cart')
def verify_1_item_in_cart(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, 'div[class="h-margin-l-x2"] span').text
    expected_text = '1 item'
    assert expected_text in actual_text, f'Expected: {expected_text}, Actual: {actual_text}'
    