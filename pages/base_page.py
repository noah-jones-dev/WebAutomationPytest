from framework.fields.link_field import LinkField
from framework.helpers.wait_utilities.wait_helper import Waits
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    def close_window(self) -> None:
        self.driver.close()
    @property
    def wait(self) -> WebDriverWait:
        return Waits.get_wait(self.driver, 10)

    ##menu links
    @property
    def admin_link(self) -> LinkField:
        return LinkField(self.driver, "Admin")
    @property
    def pim_link(self) -> LinkField:
        return LinkField(self.driver, "PIM")
    @property
    def leave_link(self) -> LinkField:
        return LinkField(self.driver, "Leave")
    @property
    def time_link(self) -> LinkField:
        return LinkField(self.driver, "Time")
    @property
    def recruitment_link(self) -> LinkField:
        return LinkField(self.driver, "Recruitment")
    @property
    def my_info_link(self) -> LinkField:
        return LinkField(self.driver, "My Info")
    @property
    def performance_link(self) -> LinkField:
        return LinkField(self.driver, "Performance")
    @property
    def dashboard_link(self) -> LinkField:
        return LinkField(self.driver, "Dashboard")
    @property
    def directory_link(self) -> LinkField:
        return LinkField(self.driver, "Directory")
    @property
    def maintenance_link(self) -> LinkField:
        return LinkField(self.driver, "Maintenance")
    @property
    def claim_link(self) -> LinkField:
        return LinkField(self.driver, "Claim")
    @property
    def buzz_link(self) -> LinkField:
        return LinkField(self.driver, "Buzz")
