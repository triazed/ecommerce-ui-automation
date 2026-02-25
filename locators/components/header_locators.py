from selenium.webdriver.common.by import By

class HeaderLocators:
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".header-links a.ico-register")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".header-links a.ico-login")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".header-links a.ico-logout")