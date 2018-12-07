from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    SELENIUM_TIMEOUT_SECONDS = 5

    def __init__(self, driver):
        self.driver = driver


    def get_title_url(self):
        return self.driver.title


    def wait_for_element_to_be_clickable(self, tuple_selector, timeout=SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(tuple_selector))


    def wait_for_visibility_of_element_located(self, tuple_selector, timeout=SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(tuple_selector))


    def wait_for_visibility_of_element(self, by, selector, timeout=SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, selector)))


    def move_to_element(self, selector, timeout=SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located(selector))
        ActionChains(self.driver).move_to_element(element).perform()


    def type_text(self, tuple_selector, value, tab=None, enter=None):
        element = self.wait_for_visibility_of_element_located(tuple_selector)
        if value:
            element.send_keys(value)
        if tab:
            element.send_keys(Keys.TAB)
        if enter:
            element.send_keys(Keys.ENTER)


    def click_element(self, tuple_selector):
        element = self.wait_for_element_to_be_clickable(tuple_selector)
        element.click()


    def is_element_visible(self, tuple_selector, timeout=SELENIUM_TIMEOUT_SECONDS):
        try:
            self.wait_for_visibility_of_element_located(tuple_selector, timeout)
            return True
        except TimeoutException:
            return False


    def get_text(self,tuple_selector):
        by = tuple_selector[0]
        selector = tuple_selector[1]
        element = self.wait_for_visibility_of_element(by, selector)
        return element.text
