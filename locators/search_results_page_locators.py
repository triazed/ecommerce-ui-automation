from selenium.webdriver.common.by import By


class SearchResultsPageLocators:

    @staticmethod
    def searched_product_name(product_name):
        searched_product = (By.XPATH, f".//div[@class='search-results']//h2[@class='product-title']/a[text()='{product_name}']")
        return searched_product

    @staticmethod
    def searched_product_add_to_cart_button(product_name):
        add_to_cart_button = (By.XPATH, f".//a[text()='{product_name}']/ancestor::div[@class='details']//button[contains(@class, 'product-box-add-to-cart-button')]")
        return add_to_cart_button

    NO_RESULT_MESSAGE = (By.CSS_SELECTOR, ".search-results div.no-result")
    SEARCH_RESULTS_PAGE_PRODUCT_NAMES = (By.CSS_SELECTOR, ".product-item .product-title")

