from selenium.webdriver.common.by import By


class RegisterPageLocators:

    # Registration form elements
    FIRST_NAME_INPUT = (By.ID, "FirstName")
    LAST_NAME_INPUT = (By.ID, "LastName")
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    PASSWORD_CONFIRM_INPUT = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")

    # Registration form validation errors
    FORM_VALIDATION_ERROR_MESSAGE = (By.CSS_SELECTOR, "div.message-error.validation-summary-errors")
    EMAIL_VALIDATION_ERROR_MESSAGE = (By.ID, "Email-error")
    PASSWORD_VALIDATION_ERROR_MESSAGE = (By.ID, "Password-error")
    CONFIRM_PASSWORD_VALIDATION_ERROR_MESSAGE = (By.ID, "ConfirmPassword-error")
    FIRST_NAME_VALIDATION_ERROR_MESSAGE = (By.ID, "FirstName-error")
    LAST_NAME_VALIDATION_ERROR_MESSAGE = (By.ID, "LastName-error")

    # Registration result page
    REGISTRATION_COMPLETED_MESSAGE = (By.CSS_SELECTOR, ".registration-result-page .result")
