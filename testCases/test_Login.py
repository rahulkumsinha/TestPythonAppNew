import pytest

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepageTitle(self, setup):
        self.logger.info("************* Test_001_Login *************")
        self.logger.info("************* verify Home Page Title ******** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* Home Page Title Test is Passed ******** ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")  # "." represent current project
            self.driver.close()
            self.logger.error("************* Home Page Title Test is Failed ******** ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("************* Verifying Login Test ******** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("************* Login Test is Passed ******** ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")  # "." represent current project
            self.driver.close()
            self.logger.error("************* Login Test is Failed ******** ")
            assert False
