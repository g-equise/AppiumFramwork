import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC
from data.config.config import *
from data.config.resources import random_card, last4dig, number_card, cvc_card


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
        # self.FLD_SELECT_CARDS = (By.XPATH, "//android.widget.TextView[@text='**** 4444']")
        # self.FLD_SELECT_CARDS = (By.XPATH, '//android.widget.TextView[@text=' + '**** ' + last4dig + ']')
        self.FLD_SELECT_CARDS = (By.XPATH, '//android.widget.TextView[@text=' + last4dig + ']')
        #        self.FLD_SELECT_CARDS = (By.XPATH, '//android.widget.TextView[@text=' + str(cardselected) + ']')
        self.BTN_REMOVE_CARD = (By.XPATH, "//android.widget.TextView[@text='Remove card']")
        self.BTN_CANCEL_CONFIRMATION = (By.ID, "android:id/button2")
        self.BTN_REMOVE_CARD_CONFIRMATION = (By.ID, "android:id/button1")

    def clickBanking(self):
        time.sleep(3)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_BANKING)).click()

    def clickHome(self):
        time.sleep(3)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_HOME)).click()

    def clickAdd(self):
        time.sleep(1)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_ADD)).click()

    def addNumberCard(self):
        print(number_card)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.FLD_NUMBER_CARD)).send_keys(
            number_card)

    def addExpDate(self):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.FLD_EXPIRATION_DATE)).send_keys(
            "01/25")

    def addCVC(self):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.FLD_CVC)).send_keys(cvc_card)

    def btn_AddCard(self):
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.BTN_ADD_CARD)).click()

    # def select_card(self):
    #     choice = random.choice(
    #         wd(self.driver, self.timeout).until(EC.presence_of_all_elements_located(self.FLD_SELECT_CARDS)))
    #     print("encontre", choice.text)
    #     choice.click()
    #     return choice.text

    def select_card(self):
        print("ESO", self.FLD_SELECT_CARDS)
        return wd(self.driver, self.timeout).until(EC.presence_of_element_located(self.FLD_SELECT_CARDS)).click()

    def remove_card(self):
        return wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.BTN_REMOVE_CARD)).click()

    def confirmation_btn_cancel(self):
        return wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.BTN_CANCEL_CONFIRMATION)).click()

    def confirmation_btn_confirm(self):
        return wd(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.BTN_REMOVE_CARD_CONFIRMATION)).click()

    # Agregar la función login.
    def addNewCard(self):
        banking = Banking(self.driver)
        banking.clickBanking()
        banking.clickAdd()
        time.sleep(1)
        banking.btn_AddCard()
        banking.addNumberCard()
        banking.addExpDate()
        banking.addCVC()
        banking.btn_AddCard()
        banking.select_card()
        banking.remove_card()
        banking.confirmation_btn_cancel()
        banking.remove_card()
        banking.confirmation_btn_confirm()
        time.sleep(2)
