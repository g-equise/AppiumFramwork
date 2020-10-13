import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC
from data.config.config import *


class Found_musicians(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.BTN_ACCESS_LOCATION_USING_APP = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        self.BTN_ACCESS_LOCATION_USING_THIS_TIME = (By.ID, 'com.android.permissioncontroller:id/permission_allow_one_time_button')
        self.BTN_ACCESS_LOCATION_DENY = (By.ID, 'com.android.permissioncontroller:id/permission_deny_button')

    def clickLocation_Using_App(self):
        time.sleep(3)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_ACCESS_LOCATION_USING_APP)).click()

    def clickLocation_Using_This_Time(self):
        time.sleep(3)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_ACCESS_LOCATION_USING_THIS_TIME)).click()

    def clickLocation_Deny(self):
        time.sleep(3)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_ACCESS_LOCATION_DENY)).click()

#Agregar la función login.
    def pay_Tips(self):
        found_mus = Found_musicians(self.driver)
        found_mus.clickLocation_Using_App()
