from selenium.webdriver.common.by import By
from selenium import webdriver
from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.set_window_size(1440, 900)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-proxy-server')

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property  # no need to add parentheses when calling method
    def logo(self):
        return self.driver.find_element(*BasePageLocators.LOGO)  # Unpack tuple with asterisk

    @property
    def navigation_links(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

    @property
    def dropdown_menu(self):
        return self.driver.find_element(*BasePageLocators.DROPDOWN)

    @property
    def dropdown_links(self):
        return self.driver.find_elements(*BasePageLocators.DROPDOWN_LINKS)

    @property
    def back_to_home_button(self):
        return self.driver.find_element(*BasePageLocators.BACK_TO_HOME)
