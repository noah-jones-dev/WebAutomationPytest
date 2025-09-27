from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from framework.fields.base_field import BaseField
from framework.helpers.verifications.verify_cell import VerifyCell

class TableField(BaseField):
    table_locator_format = "//div[@class='orangehrm-paper-container']//div[@role='table'] | //div[@class='orangehrm-paper-container'][.//*[contains(normalize-space(.), '{0}')]]//div[@role='table']"
    table_row_locator_format = ".//div[@role='row'][{0}]"
    def __init__(self, driver: WebDriver, tableName: str = None, row_class: 'TableRowField'=None):
        self.locators = [(By.XPATH, self.table_locator_format.format(tableName or ""))]
        self._row_class = row_class or TableRowField
        super().__init__(driver, self.locators)
    def __getitem__(self, row_index: int):
        """Returns a TableRowField object for the specified row index."""
        row_locators = self.locators.copy()
        row_locators.append((By.XPATH, self.table_row_locator_format.format(row_index)))
        return self._row_class(self.driver, row_locators)

class TableRowField(BaseField):
    table_cell_locator_format = ".//div[@role='cell']{0}"
    def __getitem__(self, cell_index: int):
        """Returns a TableCellField object for the specified cell index."""
        cell_locators = self.locators.copy()
        cell_locators.append((By.XPATH, self.table_cell_locator_format.format(cell_index)))
        return TableCellField(self.driver, self.locators)

class TableCellField(BaseField):
    def __init__(self, driver: WebDriver, locators: list[tuple[str, str]]):
        self.driver = driver
        self.locators = locators
    @property
    def text(self) -> str:
        """Returns the text of the cell."""
        return self.get_element().text
    @property
    def verify(self) -> VerifyCell:
        """Returns a verification object for this cell."""
        return VerifyCell(self)

    def click(self) -> None:
        """Clicks the cell."""
        self.get_element().click()