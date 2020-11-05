import unittest
from time import sleep
from appium import webdriver

from ScreenObjects.banking import Banking
from ScreenObjects.login import *
from data.config.AppiumSetup import AppiumSetup
from data.config.config import *
from data.config.desired_capabilities import *


class Testbanking(unittest.TestCase):

    def setUp(self):
        self.appium = AppiumSetup()
        self.lg = Login(self.appium.get_driver())
        self.bank = Banking(self.appium.get_driver())


    def tearDown(self):
        self.appium.close_driver()

    def test_add_credit_card(self):
        self.setUp()
        self.lg.loginAudience()
        self.bank.addNewCard()
