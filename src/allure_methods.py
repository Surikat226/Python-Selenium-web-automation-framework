import allure


class AllureMethods():
    def make_screen_and_upload(self, browser):
        windows_forbidden_symbols = ["<", ">", ":", "«", "»",
                                     "/", "|", "?", "*", "."]
        _page_title = browser.title  # временная переменная
        page_title = ''

        for i in _page_title:
            if i in windows_forbidden_symbols:
                page_title = page_title + '_'
            else:
                page_title = page_title + i

        browser.get_screenshot_as_file(f"./screenshots/{page_title}.png")
        allure.attach.file(f"./screenshots/{page_title}.png", name="Скриншот",
                           attachment_type=allure.attachment_type.PNG)
