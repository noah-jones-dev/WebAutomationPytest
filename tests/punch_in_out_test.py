import pytest
from pages.login_page import LoginPage
from pages.time_pages.punch_in_out_page import PunchInOutPage
from datetime import datetime

class TestPunchInOut:
    @pytest.fixture(scope="class", autouse=True)
    def one_time_setup(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to()
        login_page.login_user()

    def test_valid_punch_in(self, driver):
        punch_in_out = PunchInOutPage(driver)
        punch_in_out.navigate_to()
        now = datetime.now()
        formatted_date = now.strftime("%Y-%d-%m")
        formatted_time = now.strftime("%I:%M %p")
        punch_in_out.punch_in_time.clear()
        punch_in_out.punch_in_time.input(formatted_time)
        punch_in_out.punch_in_button.verify.exists()
        punch_in_out.punch_in_notes.input("Hello I am punching in now")
        punch_in_out.punch_in_button.click()
        punch_in_out.punch_in_date_time_details.verify.text_contains(f"{formatted_date} - {formatted_time}")
        punch_in_out.punch_in_note_details.verify.text_is("Hello I am punching in now")

    # def test_valid_punch_out(self, driver):
    #     pass
    #
    # def test_invalid_punch_in(self, driver):
    #     pass
    #
    # def test_invalid_punch_out(self, driver):
    #     pass
    #
    # def test_invalid_punch_out(self):
    #     pass