from selenium.webdriver.common.by import By

class LoginPageLocators:

    EMAIL_INPUT = (By.CSS_SELECTOR, "div.returning-wrapper.fieldset .email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "div.returning-wrapper.fieldset .password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "div.returning-wrapper.fieldset .login-button")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "div.message-error.validation-summary-errors li")
