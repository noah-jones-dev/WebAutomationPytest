from selenium.webdriver.ie.webdriver import WebDriver

class Windows:
    @staticmethod
    def switch_to_new_window(driver: WebDriver) -> str:
        return driver.switch_to.new_window()

    @staticmethod
    def get_current_window(driver: WebDriver) -> str:
        return driver.current_window_handle

    @staticmethod
    def get_all_windows(driver: WebDriver) -> list[str]:
        return driver.window_handles

    @staticmethod
    def switch_to_window(driver: WebDriver, window_name: str) -> None:
        return driver.switch_to.window(window_name)