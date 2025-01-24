from time import sleep

from selenium.webdriver import Keys

from pages.base_page import BasePage
from selenium.webdriver.common.by import By




class SigninPage(BasePage):
    SIGNIN_BTN = (By.ID, 'account-sign-in')
    SIGNIN_SIDENAV_BTN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    SIGNIN_PAGE_HEADER = (By.XPATH, "//button[@data-test='accountNav-signIn']")
    TERMS_AND_CONDITIONS_LINK = (By.CSS_SELECTOR, '[href*="/c/terms-conditions"]')
    def verify_signin_form_opened(self):
        expected_results = 'Sign in'
        actual_results = self.find_element(*self.SIGNIN_PAGE_HEADER).text
        assert expected_results == actual_results, f'Expected {expected_results}, but got {actual_results}'

    def open_sign_in_page(self):
        self.open_url('https://www.target.com')
        self.click(*self.SIGNIN_BTN)
        self.click(*self.SIGNIN_SIDENAV_BTN)


    def click_on_target_terms_and_conditions_link(self):
        #self.click(*self.TERMS_AND_CONDITIONS_LINK)
        terms_and_conditions = self.find_element(*self.TERMS_AND_CONDITIONS_LINK)
        terms_and_conditions.send_keys(Keys.CONTROL + Keys.RETURN)
        sleep(3)
