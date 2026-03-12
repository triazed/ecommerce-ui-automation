from locators.search_results_page_locators import SearchResultsPageLocators
from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    def click_searched_product(self, product_name):
        self.click_element(SearchResultsPageLocators.searched_product_name(product_name))

    def get_no_result_message(self):
        return self.get_text(SearchResultsPageLocators.NO_RESULT_MESSAGE)

    def click_searched_product_add_to_cart_button(self, product_name):
        self.click_element(SearchResultsPageLocators.searched_product_add_to_cart_button(product_name))
