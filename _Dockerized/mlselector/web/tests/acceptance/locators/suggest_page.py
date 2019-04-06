from selenium.webdriver.common.by import By



class SuggestPageLocators:
    ADD_SECTION = By.ID, 'question'
    DATA_TABLE = By.CLASS_NAME, 'table-responsive'
    SUGGEST_FROM = By.ID, 'suggest-form'
    SUGGEST_BUTTON = By.ID, 'add'
    SUGGESTED_ALGORITHM = By.ID, 'suggested_algorithm'
    BACK_HOMEPAGE = By.ID, 'navigation'
