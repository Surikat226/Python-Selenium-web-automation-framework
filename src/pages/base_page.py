from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


#  Это родительский класс для всех страниц
#  и он содержит базовые методы для работы со страницами
class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    """ Открыть браузер/страницу """
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

    """ Проверить, что элемент отсутствует в DOM """
    def is_element_not_presented(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until_not(EC.presence_of_element_located(locator),
                                                       message=f"Не удалось найти локатор {locator}!")
        return bool(element)

    """ Переключиться на вкладку с определённым индексом. Метод принимает индекс вкладки,
    на которую нужно перейти """
    def switch_to_another_window(self, window_index):
        self.browser.switch_to.window(self.browser.window_handles[window_index])

    """ Закрыть вкладку с определённым индексом. Метод принимает индекс вкладки, которую необходимо закрыть """
    def close_specific_window(self, window_index):
        window = self.browser.window_handles[window_index]
        self.browser.switch_to.window(window)
        self.browser.close()

    """ Проверить, что элемент кликабелен """
    def is_element_clickable(self, locator, timeout=5):
        element = WDW(self.browser, timeout).until(EC.element_to_be_clickable(locator),
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

    """ Найти все элементы с одинаковым локатором """
    def find_multiple_elements(self, locator, timeout=5):
        elements = WDW(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator),
                                                    message=f"Cant find element by locator {locator}!")
        return elements

    """ Найти КОЛИЧЕСТВО всех элементов с одинаковым локатором """
    def get_quantity_of_multiple_elements(self, locator):
        elements_quantity = self.find_multiple_elements(locator)
        return len(elements_quantity)

    """ Кликнуть на все найденные элементы с одинаковым локатором """
    def click_on_multiple_elements(self, locator, timeout=5):
        WDW(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator),
                                         message=f"Cant find element by locator {locator}!").click()

    """ Пройтись по списку всех элементов с одинаковыми локаторами и найти среди них элемент с определённым текстом.
    Метод возвращает найденный элемент, с которым можно взаимодействовать в дальнейшем """
    def find_element_with_specific_text(self, locator, text, timeout=5):
        elements = WDW(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator),
                                                    message=f"Не удалось найти локатор {locator}!")
        for element in elements:
            if element.text == text:
                return element

    """ Загрузить файл """
    def upload_file(self, locator, file_path, timeout=5):
        element = WDW(self.browser, timeout).until(EC.visibility_of_element_located(locator),
                                                   message=f"Не удалось найти локатор {locator}!")
        element.send_keys(file_path)

    """ Открыть локальный файл и получить его содержимое. На вход подаётся путь к файлу """
    def get_local_file_content(self, file_path):
        with open(file_path, "rt", encoding="utf-8") as file:
            content = file.read().rstrip()
            return content

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

    """ Метод нажимает на кнопку, поданную на его вход. Пока в работе не проверял """
    # Метод недопилен
    def press_button_on_keyboard(self, button):
        actions = ActionChains(self.browser)
        actions.send_keys(Keys).perform()
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