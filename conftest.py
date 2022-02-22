import allure
import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', \
                     action='store', \
                     default="chrome", \
                     help="Choose browser: Chrome, Firefox, Opera, Edge or Safari")

@pytest.fixture()
@allure.title('Запуск/закрытие браузера')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    if (browser_name == "Chrome"):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif (browser_name == "Firefox"):
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif (browser_name == "Opera"):
        options = webdriver.ChromeOptions()
        options.binary_location = "путь"
        browser = webdriver.Opera(options=options)
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif (browser_name == "Edge"):
        browser = webdriver.Edge()
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif (browser_name == "Safari"):
        browser = webdriver.Safari()
        browser.maximize_window()
        browser.implicitly_wait(5)
    yield browser
    time.sleep(3)
    browser.quit()