from selenium.webdriver.common.by import By
from framework.fields.button_field import ButtonField
from framework.fields.link_field import LinkField
from framework.fields.static_field import StaticField
from framework.fields.textbox_field import TextBoxField
from pages.base_page import BasePage

class LoginPage(BasePage):
    def navigate_to(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
    def login_user(self):
        self.username_input.input("Admin")
        self.password_input.input("admin123")
        self.login_button.click()
    @property
    def username_input(self):
        return TextBoxField(self.driver, textbox_name="Username")
    @property
    def password_input(self):
        return TextBoxField(self.driver, textbox_name="Password")
    @property
    def login_button(self):
        return ButtonField(self.driver, button_name="Login")
    @property
    def forgot_password_link(self):
        return LinkField(self.driver, link_name="Forgot your password")
    @property
    def username_static_hint(self):
        return StaticField(self.driver, list[(By.XPATH, "//p[contains(normalize-space(.), 'Username')]")])
    @property
    def password_static_hint(self):
        return StaticField(self.driver, list[(By.XPATH, "//p[contains(normalize-space(.), 'Password')]")])