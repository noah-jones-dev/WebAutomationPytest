from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class Waits:
    @staticmethod
    def get_wait(driver: WebDriver | WebElement, timeout: int = 10) -> WebDriverWait:
        return WebDriverWait(driver, timeout)
