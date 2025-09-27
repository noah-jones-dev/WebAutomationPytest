from framework.fields.navigation_field import NavigationField
from pages.base_page import BasePage

class TimeBasePage(BasePage):
    @property
    def timesheets_navigation(self):
        return NavigationField(self.driver, "Timesheets")
    @property
    def attendance_navigation(self):
        return NavigationField(self.driver, "Attendance")
    @property
    def reports_navigation(self):
        return NavigationField(self.driver, "Reports")
    @property
    def project_info_navigation(self):
        return NavigationField(self.driver, "Project Info")