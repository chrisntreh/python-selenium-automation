from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
    SIGNIN_BTN = (By.XPATH, "//span[@class='sc-58ad44c0-3 kkWqdY h-margin-r-x3']")

    def search_product(self):
        sleep(3)
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_signin_btn(self):
        self.click(*self.SIGNIN_BTN)