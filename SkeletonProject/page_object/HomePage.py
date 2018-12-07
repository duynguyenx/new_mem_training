from page_object import locators
from page_object.page import BasePage


class HomePage(BasePage):
    def get_text_username_thumnails(self):
        return self.get_text(locators.HOME['THUMNAILS_USER_DROPDOWN'])