from selenium.webdriver.common.by import By

class ShoppingCartPageLocators:

    PRODUCT_NAMES = (By.CSS_SELECTOR, ".cart a.product-name")

    @staticmethod
    def product_qty_in_cart(product_name):
        locator = (By.XPATH, f".//td[@class='product']/a[text()='{product_name}']/ancestor::tr//input[@class='qty-input']")
        return locator

    @staticmethod
    def remove_product_button(product_name):
        locator = (By.XPATH, f".//td[@class='product']/a[text()='{product_name}']/ancestor::tr//button[@class='remove-btn']")
        return locator

    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".order-summary-content div.no-data")

