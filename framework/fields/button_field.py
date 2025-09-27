from selenium.webdriver.common.by import By
from framework.fields.base_field import BaseField
from framework.helpers.verifications.verify_button import VerifyButton

class ButtonField(BaseField):
    locator_format = "//button[contains(normalize-space(.), '{0}')]"
    def __init__(self, driver, button_name: str=None, custom_locator: list[tuple[str, str]]=None):
        if custom_locator:
            locators = custom_locator
        elif button_name:
            locators = [(By.XPATH, self.locator_format.format(button_name))]
        else:
            raise ValueError("You must provide either button_name or custom_locator")
        super().__init__(driver, locators)
    @property
    def verify(self) -> VerifyButton:
        """Returns a verifications object for this button field."""
        return VerifyButton(self)
    def click(self) -> None:
        """Clicks the button."""
        self.get_element().click()