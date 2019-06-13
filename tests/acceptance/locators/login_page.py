from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = By.CLASS_NAME, 'form-signin'
    EMAIL_FIELD = By.ID, 'email'
    PASSWORD = By.ID, 'password'
    SUBMIT_BUTTON = By.CLASS_NAME, 'btn-login'