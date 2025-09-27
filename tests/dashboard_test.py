import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.performance_pages.employee_reviews_page import EmployeeReviewsPage
from pages.time_pages.punch_in_out_page import PunchInOutPage

class TestDashboardPage:
    @pytest.fixture(scope="class", autouse=True)
    def one_time_setup(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to()
        login_page.login_user()
    def test_open_punch_in(self, driver):
        dashboard_page = DashboardPage(driver)
        dashboard_page.navigate_to()
        dashboard_page.time_at_work_section.stop_watch_button.click()
        punch_in_out = PunchInOutPage(driver)
        punch_in_out.punch_in_button.verify.exists()
        punch_in_out.punch_in_date.verify.exists()
        punch_in_out.punch_in_notes.verify.exists()
        punch_in_out.punch_in_time.verify.exists()
    def test_pending_self_review(self, driver):
        dashboard_page = DashboardPage(driver)
        dashboard_page.navigate_to()
        dashboard_page.my_actions_section.pending_self_review_button.click()
        employee_reviews_page = EmployeeReviewsPage(driver)
        employee_reviews_page.page_static_title.verify.text_contains("Employee Reviews")
