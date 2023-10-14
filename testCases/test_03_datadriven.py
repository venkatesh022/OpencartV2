import time
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
from utilities import XLUtils
import os


class Test_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    # logger = LogGen.loggen()
    path = os.path.abspath(os.curdir) + "\\testData\\Opencart_LoginData.xlsx"

    # @pytest.mark.regression
    def test_login_ddt(self, setup):
        # self.logger.info("** Starting test_03_datadriven test **")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)     # Homepage page object class
        self.lp = LoginPage(self.driver)    # Loginpage page object class
        self.ma = MyAccountPage(self.driver)    # MyAccountpage page object class

        for r in range(2, self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.password, "Sheet1", r, 3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(3)

            self.targetPage = self.lp.isMyAccountPageExists()

            if self.exp == "Valid":
                if self.targetPage:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp == "Invalid":
                if self.targetPage:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')

        self.driver.close()

        # Final validation
        if 'Fail' not in lst_status:
            assert True
        else:
            assert False

        # self.logger.info("** End of test_03_datadriven test **")




