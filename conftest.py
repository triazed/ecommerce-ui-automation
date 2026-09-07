import pytest
from selenium import webdriver
from test_data import products
from config import urls
from pages.page_factory import PageFactory
from test_data.registration_data import new_user


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser").lower()
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"{browser} not supported. Use chrome or firefox.")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def pages(driver):
    return PageFactory(driver)

@pytest.fixture(scope="function")
def product_added_to_cart(pages):
    pages.base_ui.navigate_to(urls.BASE_URL)
    product_name = products.SEARCHED_PRODUCT_NAME_QTY_1
    pages.header.set_searched_value(product_name)
    pages.header.click_searched_product_in_search_dropdown(product_name)
    pages.product_card_page.add_product_to_cart()
    pages.header.click_close_notification_button()
    return product_name

@pytest.fixture(scope="function")
def registered_user(pages):
    pages.register_page.open()
    user = new_user()
    pages.register_page.register(user)
    pages.header.click_logout_button()
    return {
        "first_name": user['first_name'],
        "last_name": user['last_name'],
        "email": user['email'],
        "password": user['password'],
        "confirm_password": user["confirm_password"]
    }

@pytest.fixture(scope="function")
def authorized_user(pages, registered_user):
    pages.login_page.open()
    user_email, user_password = registered_user["email"], registered_user["password"]
    pages.login_page.login(user_email, user_password)
