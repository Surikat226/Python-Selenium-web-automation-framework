from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

"""Это родительский класс для всех страниц
и он содержит базовые методы для работы со страницами"""
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)

    def click_on_element(self, locator, timeout=5):
        WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                         message=f"Cant find element by locator {locator}!").click()

    def enter_text(self, locator, text, timeout=5):
        WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                         message=f"Cant find element by locator {locator}!").send_keys(text)

    def is_element_presented(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Cant find element by locator {locator}!")
        return bool(element)

    def is_element_disappeared(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until_not(EC.presence_of_element_located(locator),
                                                       message=f"Cant find element by locator {locator}!")
        return bool(element)

    def get_element_text(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Cant find element by locator {locator}!")
        return element.text

    def get_attribute_value(self, locator, attribute_name, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Cant find element by locator {locator}!")
        attribute_value = element.get_attribute(attribute_name)
        return attribute_value

    def get_page_title(self, title, timeout=5):
        title = WDW(self.browser, timeout).until(EC.title_is(title),
                                         message=f"Cant find {title} title")
        return title

    def switch_to_iframe(self, locator, timeout=5):
        WDW(self.browser, timeout).until(EC.frame_to_be_available_and_switch_to_it(locator),
                                         message=f"Cant find iframe by locator {locator}!")

    def scroll_down(self, browser):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, browser, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Cant find element by locator {locator}!")
        browser.execute_script("arguments[0].scrollIntoView();", element)