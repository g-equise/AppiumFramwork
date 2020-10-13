import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC
from data.config.config import *


class Login(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.FLD_NUMBER = (By.CLASS_NAME, 'android.widget.EditText')
        self.BTN_CONTINUE = (By.CLASS_NAME, 'android.view.View')

    def setUserNumber(self, numberDefault):
        return wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.FLD_NUMBER)).send_keys(numberDefault)

    def setUserCode(self, fld_codes):
        time.sleep(1)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.FLD_NUMBER)).send_keys(fld_codes)


    def clickContinue(self):
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.BTN_CONTINUE)).click()

#Agregar la función login.
    def loginAudience(self):
        login = Login(self.driver)
        login.setUserNumber(numberDefault)
        login.clickContinue()
        login.setUserCode(smsCode)
        login.clickContinue()
