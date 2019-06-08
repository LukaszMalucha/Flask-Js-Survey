from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = By.CLASS_NAME, 'company-logo'
    NAV_LINKS = By.CLASS_NAME, 'nav-link'
    DROPDOWN = By.ID, 'user_dropdown'
    DROPDOWN_LINKS = By.CLASS_NAME, 'dropdown-link'
    # SIDENAV_TRIGGER = By.CLASS_NAME, ''
    PAGE = By.ID, 'page-index'
