from selenium.webdriver.common.by import By

class CheckoutPageLocators:

    CHECKOUT_PAGE_TITLE = (By.CSS_SELECTOR, ".page-title h1")

    # Checkout or register section
    CHECKOUT_AS_GUEST_OR_REGISTER_H2 = (By.CSS_SELECTOR, ".checkout-as-guest-or-register-block h2")
    CHECKOUT_AS_GUEST_BUTTON = (By.CSS_SELECTOR, "button.checkout-as-guest-button")

    # Billing address section
    FIRST_NAME = (By.CSS_SELECTOR, ".edit-address #BillingNewAddress_FirstName")
    LAST_NAME = (By.CSS_SELECTOR, ".edit-address #BillingNewAddress_LastName")
    EMAIL = (By.CSS_SELECTOR, ".edit-address #BillingNewAddress_Email")
    COUNTRIES_DROPDOWN = (By.CSS_SELECTOR, ".edit-address #BillingNewAddress_CountryId")

    @staticmethod
    def country_name(country_name):
        locator = (By.XPATH, f".//div[@class='edit-address']//select[@id='BillingNewAddress_CountryId']/option[text()='{country_name}']")
        return locator

    STATES_DROPDOWN = (By.CSS_SELECTOR, ".edit-address #BillingNewAddress_StateProvinceId")

    @staticmethod
    def state_name(state_name):
        locator = (By.XPATH, f".//div[@class='edit-address']//select[@id='BillingNewAddress_StateProvinceId']/option[text()='{state_name}']")
        return locator

    CITY = (By.CSS_SELECTOR, ".edit-address #BillingNewAddress_City")
    ADDRESS_1 = (By.CSS_SELECTOR, ".edit-address #BillingNewAddress_Address1")
    ZIP_CODE = (By.CSS_SELECTOR, ".edit-address #BillingNewAddress_ZipPostalCode")
    PHONE = (By.CSS_SELECTOR, ".edit-address #BillingNewAddress_PhoneNumber")
    ADDRESS_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#billing-buttons-container button.new-address-next-step-button")

    # Shipping method section
    SHIPPING_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#shipping-method-buttons-container button.shipping-method-next-step-button")

    # Payment method section
    PAYMENT_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#payment-method-buttons-container button.payment-method-next-step-button")

    # Payment information section
    PAYMENT_INFO_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#payment-info-buttons-container button.payment-info-next-step-button")

    # Confirm order section
    PRODUCT_NAMES_IN_ORDER_SUMMARY = (By.CSS_SELECTOR, ".cart .product a.product-name")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "#confirm-order-buttons-container button.confirm-order-next-step-button")

    # Completed order section
    ORDER_COMPLETED_MESSAGE = (By.CSS_SELECTOR, ".order-completed h2.title")











