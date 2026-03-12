from selenium.webdriver.common.by import By

class HeaderLocators:
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".header-links a.ico-register")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".header-links a.ico-login")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".header-links a.ico-logout")
    CART_BUTTON = (By.CSS_SELECTOR, ".header-links a.ico-cart")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".header-lower input.search-box-text")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".header-lower button.search-box-button")
    SEARCH_DROPDOWN_PRODUCT_NAMES = (By.CSS_SELECTOR, ".search-box a.ui-menu-item-wrapper>span")
    NOTIFICATION_CLOSE_BUTTON = (By.CSS_SELECTOR, ".bar-notification .close")

    @staticmethod
    def searched_product(product_name):
        searched_product = (By.XPATH, f".//div[@role='search']//li/a[span[text()='{product_name}']]")
        return searched_product