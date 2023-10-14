import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegister import AccountRegister
import os
from utilities import randomString
from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen


class Test_001_AccountReg:
    # baseURL = "https://demo.opencart.com/"
    baseURL = ReadConfig.getApplicationURL()
    # logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self, setup):
        # self.logger.info("*** test_01_AccountReg started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.regpage = AccountRegister(self.driver)
        self.regpage.setFirstName("Henry")
        self.regpage.setLastName("James")
        self.email = randomString.random_string_generator() + "@gmail.com"
        self.regpage.setEmail(self.email)
        # self.regpage.setEmail("agc7342@gmail.com")
        self.regpage.setPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getConfirmMsg()
        self.driver.close()

        # Validation
        if self.confmsg == "Your Account Has Been Created!":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "test_account_reg.png")
            # self.logger.error("Account registration is failed")
            self.driver.close()
            assert False

        # self.logger.info("*** test_01_AccountReg finished ***")
