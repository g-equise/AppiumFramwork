import selenium
from ScreenObjects.Locators import Locator


class Login(object):

    def __init__(self, driver):
        self.fld_number = driver.find_element_by_class_name(Locator.number)
        self.btn_continue = driver.find_element_by_class_name(Locator.continueButton)
        self.fld_code = driver.find_element_by_class_name(Locator.code)

    def setUserNumber(self, fld_numbers):
        self.fld_number.send_keys(fld_numbers)

    def setUserCode(self, fld_codes):
        self.fld_code.send_keys(fld_codes)

    def ClickContinue(self):
        self.btn_continue.click()

