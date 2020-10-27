import unittest
from time import sleep
from appium import webdriver

from ScreenObjects import found_musicians
from ScreenObjects.banking import Banking
from ScreenObjects.found_musicians import Found_musicians
from ScreenObjects.login import *
from data.config.config import *
from data.config.desired_capabilities import get_desired_capabilities


class Testfoundmusicians(unittest.TestCase):

    def setUp(self):
        desired_caps = get_desired_capabilities()
        self.driver = webdriver.Remote(URLREMOTE, desired_caps)
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_fmusicians(self):
        Login.loginAudience(self)
        Found_musicians.pay_Tips(self)

#AGREGAR TARJETAS.

