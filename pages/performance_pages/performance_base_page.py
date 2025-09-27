from selenium.webdriver.common.by import By
from framework.fields.button_field import ButtonField
from framework.fields.navigation_field import NavigationField
from pages.base_page import BasePage

class PerformanceBasePage(BasePage):
    @property
    def manage_reviews_navigation(self):
        return NavigationField(self.driver, "Manage Reviews")
    @property
    def configure_navigation(self):
        return NavigationField(self.driver, "Configure")
    @property
    def my_trackers_navigation(self):
        return ButtonField(self.driver, custom_locator=[(By.XPATH, "//a[contains(text(),'My Trackers')]")])
    @property
    def more_navigation(self):
        return NavigationField(self.driver, "More")