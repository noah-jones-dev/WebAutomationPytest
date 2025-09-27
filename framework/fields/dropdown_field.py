from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from framework.fields.base_field import BaseField
from selenium.webdriver.support import expected_conditions as EC
from framework.helpers.verifications.verify_dropdown import VerifyDropdown

class DropDownField(BaseField):
    locator_format = "//div[@class='oxd-select-wrapper'][./../preceding-sibling::div/label[contains(normalize-space(.), '{0}')]]"
    def __init__(self, driver, dropdown_name: str=None, custom_locator: list[tuple[str, str]]=None):
        if custom_locator:
            locators = custom_locator
        elif dropdown_name:
            locators = [(By.XPATH, self.locator_format.format(dropdown_name))]
        else:
            raise ValueError("You must provide either button_name or custom_locator")
        super().__init__(driver, locators)
    @property
    def verify(self) -> VerifyDropdown:
        """Returns a verification object for this dropdown field."""
        return VerifyDropdown(self)
    def reveal(self) -> None:
        """Reveals the element by clicking through all locators if multiple are provided.
        Returns the last element."""
        if len(self.locators) > 1:
            for locator in self.locators[:-1]:
                try:
                    self.wait.until(EC.element_to_be_clickable(locator)).click()
                except Exception as exception:
                    print(f"Failed to click {locator}: {exception}")
        return self.wait.until(EC.element_to_be_clickable(self.locators[-1]))
    def select_option(self, option: str) -> None:
        """Clicks the desired option."""
        select = Select(self.get_element())
        select.select_by_visible_text(option)
        return self