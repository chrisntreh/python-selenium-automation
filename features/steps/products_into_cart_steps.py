from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')

@given('Search for {product}')
def search_product(context, product):
    sleep(3)
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()
    sleep(3)

@when('Add to cart')
def add_to_cart(context):
    sleep(10)
    context.driver.find_element(By.CSS_SELECTOR, '[id*="addToCartButton"]').click()
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="orderPickupButton"]').click()

@when('access cart')
def access_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[href="/cart"]').click()
    sleep(5)


@then('verify 1 item is added to cart')
def verify_1_item_in_cart(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, 'div[class="h-margin-l-x2"] span').text
    expected_text = '1 item'
    assert expected_text in actual_text, f'Expected: {expected_text}, Actual: {actual_text}'