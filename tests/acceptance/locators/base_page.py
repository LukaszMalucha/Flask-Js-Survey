from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'strong'
    NAV_LINKS = By.ID, 'navigation'
    DROPDOWN = By.ID, 'trigger'
    QUESTION_FORM = By.ID, 'question-form'
    QUESTION = By.ID, 'question'
    MATCH_BUTTON = By.ID, 'add'
    ANSWER = By.ID, 'algorithm_answer'
    PAGE = By.ID, 'page-index'
    LOGIN = By.ID, 'login'
