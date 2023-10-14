from selenium.webdriver.common.by import By


class MyAccountPage:
    # Locators
    link_logout_xpath = "//aside[@id='column-right']//a[normalize-space()='Logout']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
