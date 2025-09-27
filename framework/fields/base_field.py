from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from framework.helpers.wait_utilities.wait_helper import Waits
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseField:
    def __init__(self, driver: WebDriver, locators: list[tuple[str, str]]):
        self.driver = driver
        self.locators = locators

    def wait(self, context_element: WebDriver | WebElement=None, timeout: int=10) -> WebDriverWait:
        """Returns a WebDriverWait object."""
        if(context_element != None):
            return Waits.get_wait(context_element, timeout)
        else:
            return Waits.get_wait(self.driver, timeout)

    def get_element(self) -> WebElement:
        """Returns a WebElement for the specified field"""
        locators = self.locators
        current_element = None
        for locator in locators:
            current_element = self.wait(current_element).until(EC.presence_of_element_located(locator))
        return current_element

    def get_elements(self) -> list[WebElement]:
        """Returns all WebElements for the final locator in the chain."""
        current_context = self.driver
        for locator in self.locators[:-1]:
            parent = self.wait(current_context).until(EC.presence_of_element_located(locator))
            current_context = parent
        return self.wait(current_context).until(EC.presence_of_all_elements_located(self.locators[-1]))

    def scroll_to(self, element=None):
        """Scrolls to the specified element."""
        if element is None:
            element = self.get_element()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        wait = WebDriverWait(self.driver, 5)
        wait.until(lambda driver: driver.execute_script(
            "var elem = arguments[0];"
            "var rect = elem.getBoundingClientRect();"
            "return (rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight));",
            element
        ))
        return self