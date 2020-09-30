import unittest
from time import sleep
from appium import webdriver
from ScreenObjects.Locators import Locator
from ScreenObjects.Login import Login


class LoginAppAudience(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['deviceName'] = '44514c4d424e3098'
        desired_caps['platformName'] = 'Android'
        desired_caps['app'] = 'C:/Users/Gustavo/Downloads/app-release.apk'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_login_audience(self):
        fld_number = self.driver.find_element_by_class_name("android.widget.EditText").send_keys("2025550191")
        btn_continue = self.driver.find_element_by_class_name("android.view.View").click()
        fld_code = self.driver.find_element_by_class_name("android.widget.EditText").send_keys("190696")
        btn_continue2 = self.driver.find_element_by_class_name("android.view.View").click()
        self.driver.find_element_by_android_uiautomator()