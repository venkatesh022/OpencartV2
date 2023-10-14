# from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # Locators
    text_email_xpath = "//input[@id='input-email']"
    text_password_xpath = "//input[@id='input-password']"
    login_btn_xpath = "//button[@type='submit']"
    msg_myAccount_xpath = "//h2[text()='My Account']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_myAccount_xpath).is_displayed()
        except:
            return False
