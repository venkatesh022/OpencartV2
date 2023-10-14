from selenium.webdriver.common.by import By


class AccountRegister:
    # Locators
    text_firstname_name = "firstname"
    text_lastname_name = "lastname"
    text_email_name = "email"
    text_password_name = "password"
    check_policy_name = "agree"
    btn_continue_xpath = "//button[@type='submit']"
    # text_msg_cnfm_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"
    text_msg_cnfm_xpath = "//h1[normalize-space()='Register Account']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def setFirstName(self, fname):
        self.driver.find_element(By.NAME, self.text_firstname_name).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.NAME, self.text_lastname_name).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.text_email_name).send_keys(email)

    def setPassword(self, pwsd):
        self.driver.find_element(By.NAME, self.text_password_name).send_keys(pwsd)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME, self.check_policy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

    def getConfirmMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_cnfm_xpath).text
        except:
            None
