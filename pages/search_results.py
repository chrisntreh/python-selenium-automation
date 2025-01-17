from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SaerchResultsPage(BasePage):

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
    SEARCH_BTN = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
    ORDER_PICK_UP = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
    VIEW_CART_CHECK_OUT = (By.CSS_SELECTOR, '[href="/cart"]')

    def verify_search_results(self):
        actual_results = self.find_element(*self.SEARCH_RESULTS).text
        assert 'tea' == actual_results, f'Expected "tea", but got {actual_results}'

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)
        # self.click(*self.SEARCH_BTN)
        self.click(*self.ORDER_PICK_UP)


    def view_cart_cart_check_out(self):
        #sleep(3)
        self.click(*self.VIEW_CART_CHECK_OUT)
