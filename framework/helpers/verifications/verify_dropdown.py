from selenium.webdriver.support.select import Select
from framework.helpers.verifications.verify_base import VerifyBase

class VerifyDropdown(VerifyBase):
    def all_options_are(self, expected_options: list[str]):
        """Verify that the dropdown has the expected options."""
        select = Select(self.element)
        assert select.options == expected_options, f"The actual options {select.options} did not match {expected_options}"
    def selected_option_is(self, expected_option: str):
        """Verify that the dropdown selected option is the expected option."""
        select = Select(self.element)
        assert select.first_selected_option == expected_option, f"The actual selected option {select.first_selected_option} did not match {expected_option}"