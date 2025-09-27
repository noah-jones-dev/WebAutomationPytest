from framework.fields.button_field import ButtonField
from framework.fields.static_field import StaticField
from framework.fields.table_field import TableField, TableRowField
from selenium.webdriver.common.by import By
from pages.performance_pages.performance_base_page import PerformanceBasePage

class MyReviewsPage(PerformanceBasePage):
    def navigate_to(self):
        self.performance_link.click()
        self.manage_reviews_navigation.select_item("My Reviews")
    @property
    def records_found_static_text(self):
        return StaticField(self.driver, list[(By.XPATH, "//span[contains(normalize-space(.), 'Record')]")])
    @property
    def my_reviews_table(self):
        return self.MyReviewsTable(self.driver)

    class MyReviewsRow(TableRowField):
        @property
        def evaluate_button(self):
            button_locators = self.locators.copy()
            button_locators.append((By.XPATH, ".//button[contains(text(),'Evaluate')]"))
            return ButtonField(self.driver, custom_locator=button_locators)
        
    class MyReviewsTable(TableField):
        def __init__(self, driver):
            super().__init__(driver, tableName="My Reviews", row_class=MyReviewsPage.MyReviewsRow)

