from tests.acceptance.locators.map_page import MapPageLocators
from tests.acceptance.page_model.base_page import BasePage


class MapPage(BasePage):
    @property
    def url(self):
        return super(MapPage, self).url + '/map'


    @property
    def map_section(self):
        return self.driver.find_element(*MapPageLocators.MAP)


    @property
    def back_homepage(self):
        return self.driver.find_element(*MapPageLocators.BACK_HOMEPAGE)

