from BaseApp import BasePage
from selenium.webdriver.common.by import By


class AuthPageLocators:
    LOCATOR_LOGIN_INPUT = (By.XPATH, "//div[contains(@class, 'authentication')]//input[@name='email']")
    LOCATOR_PASSWORD_INPUT = (By.XPATH, "//div[contains(@class, 'authentication')]//input[@name='password']")
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//div[contains(@class, 'authentication')]//div[@class='button']")
    LOCATOR_ALERT_EMAIL = (By.XPATH, "//div[@class='holder email']//div[@class='error']")
    LOCATOR_ALERT_PASSWORD = (By.XPATH, "//div[@class='holder password']//div[@class='error']")
    LOCATOR_GOOGLE_BUTTON = (By.XPATH, "//div[contains(@class, 'authentication')]//div[@class='button google']")

class AuthPage(BasePage):

    def fill_login(self, login):
        login_input = self.find_element(AuthPageLocators.LOCATOR_LOGIN_INPUT)
        login_input.click()
        login_input.send_keys(login)

    def fill_password(self, password):
        password_input = self.find_element(AuthPageLocators.LOCATOR_PASSWORD_INPUT)
        password_input.click()
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.find_element(AuthPageLocators.LOCATOR_LOGIN_BUTTON)
        login_button.click()

    def find_alert_email(self):
        self.find_element(AuthPageLocators.LOCATOR_ALERT_EMAIL)
        return AuthPageLocators.LOCATOR_ALERT_EMAIL

    def find_alert_password(self):
        self.find_element(AuthPageLocators.LOCATOR_ALERT_PASSWORD)
        return AuthPageLocators.LOCATOR_ALERT_PASSWORD

    def click_google_button(self):
        google_button = self.find_element(AuthPageLocators.LOCATOR_GOOGLE_BUTTON)
        google_button.click()