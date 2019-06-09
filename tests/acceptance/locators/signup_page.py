from selenium.webdriver.common.by import By


class RegisterPageLocators:
    REGISTER_FORM = By.ID, 'form-register'
    EMAIL_FIELD = By.ID, 'email'
    USERNAME_FIELD = By.ID, 'username'
    PASSWORD = By.ID, 'password'
    CONFIRM_PASSWORD = By.ID, 'confirm'
    SUBMIT_BUTTON = By.CLASS_NAME, 'btn-login'
