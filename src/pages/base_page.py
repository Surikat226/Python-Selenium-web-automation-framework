from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


#  Это родительский класс для всех страниц
#  и он содержит базовые методы для работы со страницами
class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    """ Кликнуть по элементу """
    def click_on_element(self, locator, timeout=5):
        WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                         message=f"Cant find element by locator {locator}!").click()

    """ Найти элемент и ввести в него текст """
    def enter_text(self, locator, text, timeout=5):
        WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                         message=f"Cant find element by locator {locator}!").send_keys(text)

    """ Найти элемент и получить текст, который он содержит """
    def get_element_text(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.visibility_of_element_located(locator),
                                                   message=f"Cant find element by locator {locator}!")
        return element.text

    """ Узнать, содержится ли элемент в DOM (при этом его может не быть видно на странице).
    Результат - True или False """
    def is_element_presented(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Cant find element by locator {locator}!")
        return bool(element)

    """ Узнать, исчез ли элемент из DOM.
    Результат - True или False """
    def is_element_disappeared(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until_not(EC.presence_of_element_located(locator),
                                                       message=f"Cant find element by locator {locator}!")
        return bool(element)

    """ Получить значение атрибута элемента """
    def get_attribute_value(self, locator, attribute_name, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Cant find element by locator {locator}!")
        attribute_value = element.get_attribute(attribute_name)
        return attribute_value

    """ Получить тайтл страницы (который на вкладке) """
    def get_page_title(self, title, timeout=5):
        title = WDW(self.browser, timeout).until(EC.title_is(title),
                                                 message=f"Cant find {title} title")
        return title

    # Методы KEYS
    """ Выбрать всё содержимое элемента (Ctrl + A) """
    def select_all_text(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Cant find element by locator {locator}!")
        element.send_keys(Keys.CONTROL, 'a')

    """ Скопировать в буфер обмена (Ctrl + C) """
    def copy_to_clipboard(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Cant find element by locator {locator}!")
        element.send_keys(Keys.CONTROL, 'c')

    """ Вставить из буфера обмена (Ctrl + V) """
    def paste_from_clipboard(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Cant find element by locator {locator}!")
        element.send_keys(Keys.CONTROL, 'v')

    # /Методы KEYS

    """ Переключиться на iframe """
    def switch_to_iframe(self, locator, timeout=5):
        WDW(self.browser, timeout).until(EC.frame_to_be_available_and_switch_to_it(locator),
                                         message=f"Cant find iframe by locator {locator}!")

    """ Проскроллить вниз """
    def scroll_down(self, browser):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    """ Проскроллить к элементу """
    def scroll_to_element(self, browser, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                   message=f"Cant find element by locator {locator}!")
        browser.execute_script("arguments[0].scrollIntoView();", element)

    # Попытка написать метод смены вкладок
    # def switch_to_tab(self, browser, current_tab, new_tab, link=None):
    #     tab_list = []
    #     tab_list.append(current_tab)
    #     if len(tab_list) == 1:
    #         tab_name = browser.window_handles[0]
    #     else:
    #         tab_name = browser.window_handles[len(tab_list) + 1]
    #
    #     new_tab = browser.execute_script(f"window.open('{link}')")
    #     browser.switch_to.window(new_tab)