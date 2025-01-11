from pages.base_page import BasePage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results import SaerchResultsPage


class application:

    def __init__(self):
        self.driver = driver

        self.base_page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results = SaerchResultsPage