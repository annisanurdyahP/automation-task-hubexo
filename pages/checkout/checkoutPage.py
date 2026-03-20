import random
import string
from base.basePage import BasePage
from pages.checkout.checkoutPage_locator import CheckoutPageLocators


class CheckoutPage(BasePage):

    def clickCheckout(self):
        self.clickOnElement(CheckoutPageLocators.CHECKOUT_BUTTON)

    def fillInformation(self):
        first_name = ''.join(random.choices(string.ascii_letters, k=5))
        last_name = ''.join(random.choices(string.ascii_letters, k=5))
        postal_code = str(random.randint(10000, 99999))

        self.sendText(CheckoutPageLocators.FIRST_NAME, first_name)
        self.sendText(CheckoutPageLocators.LAST_NAME, last_name)
        self.sendText(CheckoutPageLocators.POSTAL_CODE, postal_code)

    def clickContinue(self):
        self.clickOnElement(CheckoutPageLocators.CONTINUE_BUTTON)

    def clickFinish(self):
        self.clickOnElement(CheckoutPageLocators.FINISH_BUTTON)

    def getSuccessMessage(self):
        return self.getText(CheckoutPageLocators.SUCCESS_MESSAGE)

    def clickBackHome(self):
        self.clickOnElement(CheckoutPageLocators.BACK_HOME_BUTTON)