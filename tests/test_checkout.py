from test_data import expectations
from test_data import checkout_data
import allure


@allure.parent_suite("UI Tests")
@allure.suite("Checkout")
@allure.sub_suite("Checkout tests")
class TestCheckout:

    @allure.feature("Checkout")
    @allure.story("Guest checkout")
    @allure.title("Guest user can successfully place an order")
    def test_guest_checkout_successful(self, pages, product_added_to_cart):
        pages.header.click_cart_button()
        pages.shopping_cart_page.proceed_to_checkout_from_cart()
        pages.checkout_page.click_checkout_as_guest_button()
        with allure.step("Verify checkout page is open"):
            assert pages.checkout_page.get_checkout_page_title() == expectations.CHECKOUT_PAGE_TITLE
        product = product_added_to_cart
        pages.checkout_page.set_new_user_billing_address_section(checkout_data.new_user_checkout_data())
        pages.checkout_page.continue_from_billing_address_section()
        pages.checkout_page.continue_from_shipping_method_section()
        pages.checkout_page.continue_from_payment_method_section()
        pages.checkout_page.continue_from_payment_info_section()
        checkout_page_product_names = pages.checkout_page.get_product_names_in_order_summary()
        with allure.step("Verify product is present in order summary"):
            assert len(checkout_page_product_names) == 1
            assert product in checkout_page_product_names
        pages.checkout_page.click_confirm_order_button()
        with allure.step("Verify order is completed"):
            assert pages.checkout_page.get_order_completed_message() == expectations.ORDER_COMPLETED_MESSAGE

    @allure.feature("Checkout")
    @allure.story("Authorized user checkout")
    @allure.title("Authorized user can successfully place an order")
    def test_authorized_user_checkout_successful(self, pages, product_added_to_cart, authorized_user):
        pages.header.click_cart_button()
        pages.shopping_cart_page.proceed_to_checkout_from_cart()
        with allure.step("Verify checkout page is open"):
            assert pages.checkout_page.get_checkout_page_title() == expectations.CHECKOUT_PAGE_TITLE
        product = product_added_to_cart
        pages.checkout_page.set_existing_user_billing_address_section(checkout_data.existing_user_checkout_data())
        pages.checkout_page.continue_from_billing_address_section()
        pages.checkout_page.continue_from_shipping_method_section()
        pages.checkout_page.continue_from_payment_method_section()
        pages.checkout_page.continue_from_payment_info_section()
        checkout_page_product_names = pages.checkout_page.get_product_names_in_order_summary()
        with allure.step("Verify product is present in order summary"):
            assert len(checkout_page_product_names) == 1
            assert product in checkout_page_product_names
        pages.checkout_page.click_confirm_order_button()
        with allure.step("Verify order is completed"):
            assert pages.checkout_page.get_order_completed_message() == expectations.ORDER_COMPLETED_MESSAGE
