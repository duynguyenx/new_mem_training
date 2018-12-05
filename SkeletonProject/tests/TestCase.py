import unittest
from selenium import webdriver
from page_object import locators
from page_object.LoginPage import LoginPage


class Test_Login_Gmail(unittest.TestCase):

    def setUp(self):
        url = 'http://192.168.202.48:9000' + locators.URL['LOGIN']
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)

    def test_funct_Login_Gmail(self):
        LoginPage(self.driver).input_email(locators.LOG_IN['USERNAME'])
        LoginPage(self.driver).input_password(locators.LOG_IN['PASSWORD'])
        LoginPage(self.driver).click_login_button()
        print(self.driver.title)
        self.assertTrue(self.driver.title in 'Unified | Campaigns')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
