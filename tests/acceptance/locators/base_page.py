from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = By.CLASS_NAME, 'company-logo'
    NAV_LINKS = By.XPATH, '//a[@class="nav-link"]'
    DROPDOWN = By.ID, 'user_dropdown'
    DROPDOWN_LINKS = By.CLASS_NAME, 'dropdown-link'
    SIDENAV_TRIGGER = By.CLASS_NAME, 'sidenav-trigger'
    BACK_TO_HOME = By.CLASS_NAME, 'btn-floating'
    PAGE = By.ID, 'page-index'
