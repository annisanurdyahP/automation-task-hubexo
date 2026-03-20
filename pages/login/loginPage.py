import time

from selenium.webdriver.common.by import By
from base.basePage import BasePage
from pages.login.loginPage_locator import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"


    def open(self):
        self.driver.get(self.url)

    def inputLogin(self, username, password):
        self.clearFieldText(LoginPageLocators.userNameField)
        self.sendText(LoginPageLocators.userNameField, username)
        self.clearFieldText(LoginPageLocators.passwordField)
        self.sendText(LoginPageLocators.passwordField, password)
        self.clickOnElement(LoginPageLocators.loginButton)


    def clickLogout(self):
        self.wait_until_visible(LoginPageLocators.burgerMenuButton)
        self.clickOnElement(LoginPageLocators.burgerMenuButton)
        self.wait_until_visible(LoginPageLocators.logoutButton)
        self.clickOnElement(LoginPageLocators.logoutButton)

    def verifyLogoutSuccessful(self):
        self.wait_until_visible(LoginPageLocators.loginButton)


    def getErrorMessage(self):
        error_message_element = self.wait_until_visible(LoginPageLocators.ERROR_MESSAGE)
        return error_message_element.text