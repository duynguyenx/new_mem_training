# driver = webdriver.Chrome()
# url = "http://192.168.202.48:9000/login"
# driver.get(url)
# page = BasePage(driver)
# page.type_text(MainPageLocators.LOG_IN['EMAIL_TEXTBOX'],"duy.nguyen@unified.com")
# page.type_text(MainPageLocators.LOG_IN['PASSWORD_TEXTBOX'],"Unified123!")
# wait = WebDriverWait(driver, 5)
# element = wait.until(EC.visibility_of_element_located(MainPageLocators.LOG_IN['LOGIN_BUTTON']))
# sumitbutton = driver.find_element(*MainPageLocators.LOGIN_BUTTON)
# action=ActionChains(driver)
# action.move_to_element(sumitbutton)
# action.perform()
import re
from page_object import locators


string = locators.HOME['THUMNAILS_USER_DROPDOWN']
By = 'By.'
print(string)