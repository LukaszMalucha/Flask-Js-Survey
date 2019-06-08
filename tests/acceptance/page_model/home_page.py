from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/'  # access super class

    @property  # no need to add parentheses when calling method
    def map_link(self):
        return self.driver.find_element(*HomePageLocators.MAP_LINK)  # Unpack tuple with asterisk
