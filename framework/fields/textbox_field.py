from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from framework.fields.base_field import BaseField
from framework.helpers.verifications.verify_textbox import VerifyTextbox

class TextBoxField(BaseField):
    locator_format = "//input[contains(normalize-space(.), '{0}')] | //input[contains(@placeholder, '{0}')] | //textarea[contains(normalize-space(.), '{0}')] | //textarea[contains(@placeholder, '{0}')]"
    def __init__(self, driver, textbox_name: str=None, custom_locator: list[tuple[str, str]]=None):
        if custom_locator:
            locators = custom_locator
        elif textbox_name:
            locators = [(By.XPATH, self.locator_format.format(textbox_name))]
        else:
            raise ValueError("You must provide either button_name or custom_locator")
        super().__init__(driver, locators)
    @property
    def verify(self) -> VerifyTextbox:
        """Returns a verification object for this text field"""
        return VerifyTextbox(self)
    def input(self, text: str) -> 'TextBoxField':
        """Input text into the textbox."""
        self.get_element().send_keys(text)
        return self
    def hit_enter(self) -> 'TextBoxField':
        """Press the Enter key."""
        self.get_element().send_keys(Keys.ENTER)
        return self
    def clear(self):
        """Clears the textbox."""
        self.get_element().clear()