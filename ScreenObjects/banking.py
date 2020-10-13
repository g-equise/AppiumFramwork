import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC
from data.config.config import *


class Banking(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.BTN_BANKING = (By.XPATH, "//android.widget.TextView[@text='Banking']")
        self.BTN_HOME = (By.CLASS_NAME, 'android.view.View')
        self.BTN_ADD = (By.XPATH, "//android.view.ViewGroup[@index='1' and @clickable='true']")
        self.FLD_NUMBER_CARD = (By.XPATH, "//android.widget.EditText[@text='0000 0000 0000 0000']")
        self.FLD_EXPIRATION_DATE = (By.XPATH, "//android.widget.EditText[@text='MM/YY']")
        self.FLD_CVC = (By.XPATH, "//android.widget.EditText[@text='CVC']")
        self.BTN_ADD_CARD = (By.XPATH, "//android.widget.TextView[@text='Add card']")
#        self.BTN_ADD_CARD = (By.XPATH, "//android.widget.TextView[contains(@text='Add card')]")
        self.FLD_SELECT_CARDS = (By.XPATH, "//android.widget.TextView[@text='**** ']")

    def clickBanking(self):
        time.sleep(3)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_BANKING)).click()

    def clickHome(self):
        time.sleep(3)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_HOME)).click()

    def clickAdd(self):
        time.sleep(1)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_ADD)).click()

    def addNumberCard(self, card_supported):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.FLD_NUMBER_CARD)).send_keys(card_supported)

    def AddExpDate(self, expiration_date):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.FLD_EXPIRATION_DATE)).send_keys(expiration_date)

    def AddCVC(self):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.FLD_CVC)).send_keys("123")

    def btn_AddCard(self):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_ADD_CARD)).click()

    def select_card(self):
        time.sleep(2)
        choice = random.choice(wd(self.driver, self.timeout).until(EC.presence_of_all_elements_located(self.FLD_SELECT_CARDS)))
        print(choice.text)
        return choice.text


    #Agregar la función login.
    def enterBanking(self):
        banking = Banking(self.driver)
        banking.clickBanking()
        banking.clickAdd()
        time.sleep(1)
        banking.btn_AddCard()
        banking.addNumberCard(CardSupported)
        banking.AddExpDate(ExpirationDate)
        banking.AddCVC()
        banking.btn_AddCard()
        banking.select_card()
        time.sleep(5)
