from selenium.webdriver.common.by import By
from base_page import  BasePage


class SaerchResultsPage(BasePage):
    def verify_search_results(self):
        actual_results = self.find_element(*self.SEARCH_RESULTS).text
        assert 'tea' == actual_results, f'Expected {tea}, but got {actual_results}'
