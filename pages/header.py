from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from time import sleep
from base_page import  BasePage
from features.steps.product_search import input_search


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, 'search_btn')

    def search_product(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(self.SEARCH_BTN)
        sleep(10)
