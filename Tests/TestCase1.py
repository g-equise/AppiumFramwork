import unittest
from time import sleep
from appium import webdriver
from ScreenObjects.Locators import Locator
from ScreenObjects.Login import Login
from data.config.desired_capabilities import get_desired_capabilities


class LoginAppAudience(unittest.TestCase):

    def setUp(self):
        desired_caps = get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_login_audience(self):
        login = Login(self.driver)
        sleep(5)
        login.setUserNumber(Locator.numberDefault)
        sleep(4)
        login.ClickContinue()
        sleep(4)
        login.setUserCode(Locator.smsCode)
        sleep(4)
        login.ClickContinue()
        sleep(4)
