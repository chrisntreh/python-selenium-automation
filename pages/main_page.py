from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    SIGNIN_BTN = (By.XPATH, "//span[@class='sc-58ad44c0-3 kkWqdY h-margin-r-x3']")

    def open_main_page(self):
        self.open_url('https://www.target.com/')

