from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

    @property
    def form(self):
        return self.driver.find_element(*BasePageLocators.QUESTION_FORM)

    @property
    def dropdown(self):
        return self.driver.find_element(*BasePageLocators.DROPDOWN)

    @property
    def question(self):
        return self.driver.find_elements(*BasePageLocators.QUESTION)

    @property
    def match_button(self):
        return self.driver.find_element(*BasePageLocators.MATCH_BUTTON)

    @property
    def answer(self):
        return self.driver.find_element(*BasePageLocators.ANSWER)

    def form_field(self, name):
        return self.form.find_element(By.ID, name)

    @property
    def login(self):
        return self.driver.find_element(*BasePageLocators.LOGIN)