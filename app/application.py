from pages.base_page import BasePage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results import SaerchResultsPage
from pages.signin_page import SigninPage
from pages.verify_item import VerifyItem

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results = SaerchResultsPage(driver)
        self.signin_page = SigninPage(driver)
        self.verify_item = VerifyItem(driver)
