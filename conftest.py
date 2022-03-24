import pytest
import allure
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="Chrome",
                     help="Choose browser: Chrome, Firefox, Opera, Edge or Safari")

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == "Chrome":
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif browser_name == "Firefox":
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif browser_name == "Opera":
        browser = webdriver.Opera(executable_path=OperaDriverManager().install())
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif browser_name == "Edge":
        browser = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif browser_name == "Safari":
        browser = webdriver.Safari()
        browser.maximize_window()
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError("'--browser_name' should be 'Chrome, Firefox, Opera, Edge or Safari'")

    yield browser
    time.sleep(3)
    browser.quit()