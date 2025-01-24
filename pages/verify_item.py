from pages.base_page import BasePage
from selenium.webdriver.common.by import By




class VerifyItem(BasePage):

    Verify_Item = (By.CSS_SELECTOR, 'div[class="h-margin-l-x2"] span')

    def verify_1_item_in_cart(self):
        expected_text = '1 item'
        actual_results = self.find_element(*self.VerifyItem).text
        assert expected_text in actual_results, f'Expected: {expected_text}, Actual: {actual_results}'
