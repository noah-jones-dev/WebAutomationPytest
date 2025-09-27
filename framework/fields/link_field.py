from selenium.webdriver.common.by import By
from framework.fields.base_field import BaseField
from framework.helpers.verifications.verify_link import VerifyLink

class LinkField(BaseField):
    locator_format = "//a[contains(normalize-space(.), '{0}')] | //p[contains(normalize-space(.), '{0}')]"
    def __init__(self, driver, link_name: str=None, custom_locator: list[tuple[str, str]]=None):
        if custom_locator:
            locators = custom_locator
        elif link_name:
            locators = [(By.XPATH, self.locator_format.format(link_name))]
        else:
            raise ValueError("You must provide either button_name or custom_locator")
        super().__init__(driver, locators)
    @property
    def verify(self) -> VerifyLink:
        """Returns a verification object for this cell."""
        return VerifyLink(self)
    def click(self) -> None:
        """Clicks the link."""
        self.get_element().click()