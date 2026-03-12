from selenium.webdriver.common.by import By

class ProductCardPageLocators:

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-name h1")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart button.add-to-cart-button")
    ADD_TO_CART_QUANTITY_INPUT = (By.CSS_SELECTOR, ".add-to-cart input.qty-input")
    MIN_QUANTITY_NOTIFICATION = (By.CSS_SELECTOR, ".add-to-cart div.min-qty-notification")

