from selenium.webdriver.common.by import By

class RegisterPageLocators:

    # Registration form
    FIRST_NAME_INPUT = (By.ID, "FirstName")
    LAST_NAME_INPUT = (By.ID, "LastName")
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    PASSWORD_CONFIRM_INPUT = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")

    # Registration result page
    REGISTRATION_COMPLETED_MESSAGE = (By.CSS_SELECTOR, ".registration-result-page .result")
