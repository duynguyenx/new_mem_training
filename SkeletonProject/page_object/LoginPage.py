from page_object import locators
from page_object.page import BasePage


class LoginPage(BasePage):

    def input_email(self, email):
        self.type_text(locators.LOG_IN['EMAIL_TEXTBOX'], email)


    def input_password(self, password):
        self.type_text(locators.LOG_IN['PASSWORD_TEXTBOX'], password)


    def click_login_button(self):
        self.click_element(locators.LOG_IN['LOGIN_BUTTON'])


    def get_text_username_thumnails(self,by, selector):
        self.get_text(by,selector)