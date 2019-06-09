from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/'  # access super class

    @property
    def question_form(self):
        return self.driver.find_element(*HomePageLocators.QUESTION_FORM)

    @property
    def form_title(self):
        return self.driver.find_element(*HomePageLocators.FORM_TITLE)

    @property
    def question(self):
        return self.driver.find_element(*HomePageLocators.QUESTION)

    @property
    def next_button(self):
        return self.driver.find_element(*HomePageLocators.NEXT_BUTTON)

    @property
    def complete_button(self):
        return self.driver.find_element(*HomePageLocators.COMPLETE_BUTTON)


