from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')


@then('verify 14 benefit cells are there')
def verify_ten_cells(context):
    expected_results = 14
    actual_results=context.driver.find_elements(By.CSS_SELECTOR, '[class="cell-item-content"]')
    assert expected_results == len(actual_results), f'Expected {expected_results}, but got {actual_results}'
    sleep(8)



