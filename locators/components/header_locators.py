from selenium.webdriver.common.by import By

class HeaderLocators:
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".header-links a.ico-register")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".header-links a.ico-login")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".header-links a.ico-logout")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".header-lower input.search-box-text")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".header-lower button.search-box-button")
    SEARCH_DROPDOWN_PRODUCT_NAMES = (By.CSS_SELECTOR, ".search-box a.ui-menu-item-wrapper>span")
    SEARCH_DROPDOWN_LIST = (By.CSS_SELECTOR, ".search-box li")

    @staticmethod
    def searched_product(product_name):
        searched_product = (By.XPATH, f".//div[@role='search']//li/a[span[text()='{product_name}']]")
        return searched_product