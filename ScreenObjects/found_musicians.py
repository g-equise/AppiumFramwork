import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC
from data.config.config import *


class Found_musicians(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.BTN_GIVE_TIPS = (By.XPATH, "//android.widget.TextView[@text='Give tips']")
        self.BTN_FOUND = (By.XPATH, "//android.view.ViewGroup[@index='1']")
        self.FLD_SELECT_AXEL = (By.XPATH, "//android.widget.TextView[@text='Axel Navarro']")
        self.FLD_SELECT_CUSTOM_AMOUNTS = (By.XPATH, "//android.view.ViewGroup[@index='0']")
        self.FLD_SELECT_20_AMOUT = (By.XPATH, "//android.widget.TextView[@text='$20']")
        self.BTN_PAY_TIPS = (By.XPATH, "//android.widget.TextView[@text='Pay tips']")
        self.BTN_ACCESS_LOCATION_USING_APP = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        self.BTN_ACCESS_LOCATION_USING_THIS_TIME = (By.ID, 'com.android.permissioncontroller:id/permission_allow_one_time_button')
        self.BTN_ACCESS_LOCATION_DENY = (By.ID, 'com.android.permissioncontroller:id/permission_deny_button')

    def click_give_tips(self):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_GIVE_TIPS)).click()

    def click_found(self):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_FOUND)).click()

    def click_axel(self):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.FLD_SELECT_AXEL)).click()

    def click_custom_amounts(self):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.FLD_SELECT_CUSTOM_AMOUNTS)).click()

    def click20(self):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.FLD_SELECT_20_AMOUT)).click()

    def clickPayTips(self):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_PAY_TIPS)).click()

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
        found_mus.click_give_tips()
        found_mus.click_found()
        found_mus.click_axel()
        found_mus.click20()
        found_mus.clickPayTips()
        time.sleep(5)
