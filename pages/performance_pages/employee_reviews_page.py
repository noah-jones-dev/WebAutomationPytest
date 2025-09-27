from selenium.webdriver.common.by import By
from framework.fields.static_field import StaticField
from pages.performance_pages.performance_base_page import PerformanceBasePage

class EmployeeReviewsPage(PerformanceBasePage):
    def navigate_to(self):
        self.performance_link.click()
        self.manage_reviews_navigation.select_item("Employee Reviews")

    @property
    def page_static_title(self):
        return StaticField(self.driver, [(By.XPATH, "//h5")])
