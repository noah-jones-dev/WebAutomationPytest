from selenium.webdriver.common.by import By
from framework.fields.base_field import BaseField
from framework.fields.button_field import ButtonField
from pages.base_page import BasePage

class DashboardPage(BasePage):
    section_locator_format = "//div[contains(@class, 'oxd-grid-item')][.//p[contains(normalize-space(.), '{0}')]]"
    def navigate_to(self):
        self.dashboard_link.click()
    @property
    def time_at_work_section(self):
        return self.TimeAtWorkSection(self.driver)
    @property
    def my_actions_section(self):
        return self.MyActionsSection(self.driver)
    class TimeAtWorkSection(BaseField):
        def __init__(self, driver):
            locators = [(By.XPATH, DashboardPage.section_locator_format.format("Time at Work"))]
            super().__init__(driver, locators)
        @property
        def stop_watch_button(self):
            button_locator = self.locators.copy()
            button_locator.append((By.XPATH, ".//button"))
            return ButtonField(self.driver, custom_locator=button_locator)
    class MyActionsSection(BaseField):
        button_locator_format = ".//button[following-sibling::p[contains(normalize-space(.), '{0}')]]"
        def __init__(self, driver):
            locators = [(By.XPATH, DashboardPage.section_locator_format.format("My Actions"))]
            super().__init__(driver, locators)
        @property
        def pending_self_review_button(self):
            button_locator = self.locators.copy()
            button_locator.append((By.XPATH, self.button_locator_format.format("Pending Self Review")))
            return ButtonField(self.driver, custom_locator=button_locator)
        @property
        def candidate_to_interview_button(self):
            button_locator = self.locators.copy()
            button_locator.append((By.XPATH, self.button_locator_format.format("Candidate to Interview")))
            return ButtonField(self.driver, custom_locator=button_locator)

