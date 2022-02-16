from BaseApp import BasePage
from selenium.webdriver.common.by import By


class GamePageLocators:
    LOCATOR_LK_BUTTON = (By.XPATH, "//span[@class='user__full-name']")



class GamePage(BasePage):
    def find_lk_button(self):
        find_lk_button = self.find_element(GamePageLocators.LOCATOR_LK_BUTTON)