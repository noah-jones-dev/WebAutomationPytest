from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from framework.fields.base_field import BaseField

class NavigationField(BaseField):
    locator_format = "//li[contains(@class, 'oxd-topbar-body-nav-tab')][./span[contains(normalize-space(.), '{0}')]]"
    def __init__(self, driver, navigation_name: str=None, custom_locator: list[tuple[str, str]]=None):
        if custom_locator:
            locators = custom_locator
        elif navigation_name:
            locators = [(By.XPATH, self.locator_format.format(navigation_name))]
            locators.append((By.XPATH, "//li[./ancestor::ul[@class='oxd-dropdown-menu']]"))
        else:
            raise ValueError("You must provide either button_name or custom_locator")
        super().__init__(driver, locators)

    # @property
    # def verify(self) -> VerifyDropdown:
    #     """Returns a verification object for this dropdown field."""
    #     return VerifyDropdown(self)

    def reveal(self):
        """Reveals dropdowns by clicking through all locators except the last one."""
        if len(self.locators) > 1:
            for locator in self.locators[:-1]:
                try:
                    self.wait().until(EC.element_to_be_clickable(locator)).click()
                except Exception as exception:
                    print(f"Failed to click {locator}: {exception}")
        return self.wait().until(EC.element_to_be_clickable(self.locators[-1]))

    def select_item(self, item_text):
        """Selects an item from the list by its text."""
        self.reveal()
        elements = self.get_elements()
        for element in elements:
            if item_text in element.text:
                element.click()
                return
        raise ValueError(f"Item '{item_text}' not found in the list.")