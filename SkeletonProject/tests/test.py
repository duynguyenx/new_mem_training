from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from hamcrest import assert_that,equal_to

driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = "http://192.168.202.48:9000/login"
driver.get(url)
expected_Title = 'Unified | Campaigns'
expected_Username ='Duy'
username = "duy.nguyen@unified.com"
password = "Unified123!"

def func_Login_successfully():
    element_Email_txtbox = driver.find_element(By.ID, 'email-login')
    element_Password_txtbox = driver.find_element(By.NAME, 'password')
    element_Login_btn = driver.find_element(By.ID, 'submit')
    element_Email_txtbox.send_keys(username)
    element_Password_txtbox.send_keys(password)
    element_Login_btn.click()
    actual_Title = driver.title
    print(actual_Title)
    # lambda actual_Title : print('true') if actual_Title == expected_Title else print('false')
    if (actual_Title == expected_Title):
        print('true')
    element_User_thumnail = driver.find_element(By.XPATH,'//*[@id="bodyWrapper"]/div[1]/nav/div[1]/ul[2]/li[2]/a/span[2]')
    txt_Username_label = element_User_thumnail.text
    print(txt_Username_label)
    if (txt_Username_label == expected_Username):
        print('True')
    driver.quit()
def func_Check_dynamic_table():
    print('từ từ chi build')

if __name__ == "__main__":
    func_Login_successfully()
