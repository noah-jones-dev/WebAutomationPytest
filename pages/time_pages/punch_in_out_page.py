from selenium.webdriver.common.by import By

from framework.fields.button_field import ButtonField
from framework.fields.static_field import StaticField
from framework.fields.textbox_field import TextBoxField
from pages.time_pages.time_base_page import TimeBasePage

class PunchInOutPage(TimeBasePage):
    def navigate_to(self):
        self.time_link.click()
        self.attendance_navigation.select_item("Punch In/Out")
    @property
    def punch_in_date(self):
        return TextBoxField(self.driver, textbox_name="yyyy-dd-mm")
    @property
    def punch_in_time(self):
        return TextBoxField(self.driver, textbox_name="hh:mm")
    @property
    def punch_in_notes(self):
        return TextBoxField(self.driver, textbox_name="Type here")
    @property
    def punch_in_button(self):
        return ButtonField(self.driver, button_name="In")
    @property
    def punch_out_button(self):
        return ButtonField(self.driver, button_name="Out")
    @property
    def punch_in_date_time_details(self):
        return StaticField(self.driver, [(By.XPATH, "//div[./label[contains(normalize-space(.), 'Punched in time')]]/following-sibling::div/p")])

    @property
    def punch_in_note_details(self):
        return StaticField(self.driver, [(By.XPATH, "//div[./label[contains(normalize-space(.), 'Punched In Note')]]/following-sibling::div/p")])