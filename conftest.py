import pytest
from selenium import webdriver
import time

@pytest.fixture()
def browser():
    browser = webdriver.Chrome(executable_path="Диск:/Путь/К/Драйверу.exe")
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    time.sleep(3)
    browser.quit()