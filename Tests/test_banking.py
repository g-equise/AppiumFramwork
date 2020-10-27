import unittest
from time import sleep
from appium import webdriver

from ScreenObjects.banking import Banking
from ScreenObjects.login import *
from data.config.config import *
from data.config.desired_capabilities import get_desired_capabilities


class Testbanking(unittest.TestCase):

    def setUp(self):
        desired_caps = get_desired_capabilities()
        self.driver = webdriver.Remote(URLREMOTE, desired_caps)
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_add_credit_card(self):
        Login.loginAudience(self)
        Banking.addNewCard(self)

#AGREGAR TARJETAS.

