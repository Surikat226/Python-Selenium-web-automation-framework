import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', \
                     action='store', \
                     default="chrome", \
                     help="Choose browser: chrome or firefox")

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if (browser_name == "chrome"):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif (browser_name == "firefox"):
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.maximize_window()
        browser.implicitly_wait(5)
    yield browser
    time.sleep(3)
    browser.quit()