from selenium.webdriver.common.by import By

from tests.acceptance.locators.add_page import SuggestPageLocators
from tests.acceptance.page_model.base_page import BasePage


class SuggestPage(BasePage):
    @property
    def url(self):
        return super(SuggestPage, self).url + '/add_algorithm'

    @property
    def add_section(self):
        return self.driver.find_element(*SuggestPageLocators.ADD_SECTION)

    @property
    def form(self):
        return self.driver.find_element(*SuggestPageLocators.SUGGEST_FROM)

    @property
    def data_table(self):
        return self.driver.find_element(*SuggestPageLocators.DATA_TABLE)

    @property
    def suggest_button(self):
        return self.driver.find_element(*SuggestPageLocators.SUGGEST_BUTTON)

    @property
    def suggested_algorithm(self):
        return self.driver.find_elements(*SuggestPageLocators.SUGGESTED_ALGORITHM)


    @property
    def back_homepage(self):
        return self.driver.find_element(*SuggestPageLocators.BACK_HOMEPAGE)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)

