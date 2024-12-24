from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, '[data-module-type="ProductDetailVariationSelector"] div:nth-child(3) ul')

SELECTED_COLOR = (By.CSS_SELECTOR, '[data-module-type="ProductDetailVariationSelector"] div:nth-child(3) ul li')


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/A-91511634?preselect=93148522{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['grey', 'navy/tan', 'white/sand/tan', 'white/navy/red - Out of Stock']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()

        SELECTED_COLOR = (By.CSS_SELECTOR, '[data-test="@web/VariationComponent"]:nth-child(3) div')
        print('Current color', SELECTED_COLOR.text)

        SELECTED_COLOR = SELECTED_COLOR.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(SELECTED_COLOR)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
