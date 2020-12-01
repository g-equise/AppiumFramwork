from appium.webdriver import webdriver
from appium import webdriver

from data.config.config import URLREMOTE
from data.config.desired_capabilities import get_desired_capabilities_bs, BROWSERSTACK_URL, get_desired_capabilities


class AppiumSetup:

    def __init__(self):
        #desired_caps = get_desired_capabilities()
        #self.driver = webdriver.Remote(URLREMOTE, desired_caps)
        desired_caps = get_desired_capabilities_bs()
        self.driver = webdriver.Remote(BROWSERSTACK_URL, desired_caps)
        self.driver.set_location(-34.6344903, -58.4494996, 10)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()
