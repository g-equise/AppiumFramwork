import unittest
from time import sleep
from appium import webdriver

from ScreenObjects import found_musicians
from ScreenObjects.banking import Banking
from ScreenObjects.found_musicians import Found_musicians
from ScreenObjects.login import *
from data.config.AppiumSetup import AppiumSetup
from data.config.config import *
from data.config.desired_capabilities import get_desired_capabilities, get_desired_capabilities_bs, BROWSERSTACK_URL


class Testfoundmusicians(unittest.TestCase):

    def setUp(self):
        self.appium = AppiumSetup()
        self.lg = Login(self.appium.get_driver())
        self.found = Found_musicians(self.appium.get_driver())


    def test_fmusicians(self):
        self.lg.loginAudience()
        self.found.pay_Tips()
        self.appium.close_driver()


