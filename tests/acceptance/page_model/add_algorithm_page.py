from selenium.webdriver.common.by import By

from tests.acceptance.locators.add_algorithm_page import AddAlgorithmPageLocators
from tests.acceptance.page_model.base_page import BasePage


class AddAlgorithmPage(BasePage):
    @property
    def url(self):
        return super(AddAlgorithmPage, self).url + '/add_algorithm'

    @property
    def form(self):
        return self.driver.find_element(*AddAlgorithmPageLocators.ADD_FORM)

    @property
    def data_table(self):
        return self.driver.find_element(*AddAlgorithmPageLocators.DATA_TABLE)

    @property
    def add_button(self):
        return self.driver.find_element(*AddAlgorithmPageLocators.ADD_BUTTON)

    @property
    def algorithms(self):
        return self.driver.find_elements(*AddAlgorithmPageLocators.ALGORITHM)


    def form_field(self, name):
        return self.form.find_element(By.NAME, name)

