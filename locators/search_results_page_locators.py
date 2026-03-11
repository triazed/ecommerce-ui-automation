from selenium.webdriver.common.by import By


class SearchResultsPageLocators:

    @staticmethod
    def searched_product_name(product_name):
        searched_product = (By.XPATH, f".//div[@class='search-results']//h2[@class='product-title']/a[text()='{product_name}']")
        return searched_product

    NO_RESULT_MESSAGE = (By.CSS_SELECTOR, ".search-results div.no-result")