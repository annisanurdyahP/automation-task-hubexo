from base.basePage import BasePage
from pages.cart.cartPage_locator import CartPageLocators


class CartPage(BasePage):

    def getProductName(self):
        return self.getText(CartPageLocators.PRODUCT_NAME_CART)

    def getProductQuantity(self):
        return self.getText(CartPageLocators.PRODUCT_QTY)