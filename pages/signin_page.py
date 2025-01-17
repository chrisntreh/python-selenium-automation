from pages.base_page import BasePage
from selenium.webdriver.common.by import By




class SigninPage(BasePage):

    SIGNIN_PAGE_HEADER = (By.XPATH, "//button[@data-test='accountNav-signIn']")

    def verify_signin_form_opened(self):
        expected_results = 'Sign in'
        actual_results = self.find_element(*self.SIGNIN_PAGE_HEADER).text
        assert expected_results == actual_results, f'Expected {expected_results}, but got {actual_results}'

