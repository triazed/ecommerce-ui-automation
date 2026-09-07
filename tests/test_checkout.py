from test_data import expectations
from test_data import checkout_data


class TestCheckout:

    def test_guest_checkout_successful(self, pages, product_added_to_cart):
        pages.header.click_cart_button()
        pages.shopping_cart_page.proceed_to_checkout_from_cart()
        pages.checkout_page.click_checkout_as_guest_button()
        assert pages.checkout_page.get_checkout_page_title() == expectations.CHECKOUT_PAGE_TITLE
        product = product_added_to_cart
        pages.checkout_page.set_new_user_billing_address_section(checkout_data.new_user_checkout_data())
        pages.checkout_page.continue_from_billing_address_section()
        pages.checkout_page.continue_from_shipping_method_section()
        pages.checkout_page.continue_from_payment_method_section()
        pages.checkout_page.continue_from_payment_info_section()
        checkout_page_product_names = pages.checkout_page.get_product_names_in_order_summary()
        assert len(checkout_page_product_names) == 1
        assert product in checkout_page_product_names
        pages.checkout_page.click_confirm_order_button()
        assert pages.checkout_page.get_order_completed_message() == expectations.ORDER_COMPLETED_MESSAGE

    def test_authorized_user_checkout_successful(self, pages, product_added_to_cart, authorized_user):
        pages.header.click_cart_button()
        pages.shopping_cart_page.proceed_to_checkout_from_cart()
        assert pages.checkout_page.get_checkout_page_title() == expectations.CHECKOUT_PAGE_TITLE
        product = product_added_to_cart
        pages.checkout_page.set_existing_user_billing_address_section(checkout_data.existing_user_checkout_data())
        pages.checkout_page.continue_from_billing_address_section()
        pages.checkout_page.continue_from_shipping_method_section()
        pages.checkout_page.continue_from_payment_method_section()
        pages.checkout_page.continue_from_payment_info_section()
        checkout_page_product_names = pages.checkout_page.get_product_names_in_order_summary()
        assert len(checkout_page_product_names) == 1
        assert product in checkout_page_product_names
        pages.checkout_page.click_confirm_order_button()
        assert pages.checkout_page.get_order_completed_message() == expectations.ORDER_COMPLETED_MESSAGE
