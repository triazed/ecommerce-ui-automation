import pytest
from selenium import webdriver
from pages.page_factory import PageFactory


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
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


@pytest.fixture
def pages(driver):
    return PageFactory(driver)
