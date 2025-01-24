from features.steps.terms_and_conditions_steps import verify_terms_and_conditions_page_is_open
from pages. verify_terms_and_conditions_page_is_open import VerifyTermsAndConditionsPageIsOpen

class VerifyTermsAndConditionsPageIsOpen(verify_terms_and_conditions_page_is_open()):

    def verify_terms_and_condition (self):
        self.open_url('https://www.target.com/c/terms-conditions/-/N-4sr7l')
