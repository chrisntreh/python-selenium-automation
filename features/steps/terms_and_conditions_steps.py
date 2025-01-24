from behave import given, when, then
from time import sleep

@given('Open sign in page')
def open_sign_in_page(context):
    context.app.signin_page.open_sign_in_page()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()


@when('Click on Target terms and conditions link')
def click_on_target_terms_and_conditions_link(context):
    context.app.signin_page.click_on_target_terms_and_conditions_link()


@when('Switch to the newly opened window')
def switch_to_newly_open_window(context):
    context.app.base_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page_is_open(context):
    context.app.verify_terms_and_conditions_page_is_open()


@then('User can close new window and switch back to original')
def user_can_close_new_window_and_switch_to_origbial(context):
    context.app.user_can_close_new_window_and_switch_to_origbial()