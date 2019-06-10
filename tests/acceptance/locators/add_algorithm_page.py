from selenium.webdriver.common.by import By



class AddAlgorithmPageLocators:
    DATA_TABLE = By.CLASS_NAME, 'table-responsive'
    ADD_FORM = By.ID, 'add-form'
    ADD_BUTTON = By.ID, 'addButton'
    DELETE_BUTTON = By.CLASS_NAME, 'delete-button'
    SUGGESTED_ALGORITHM_ROW = By.CLASS_NAME, 'odd gradeA'
