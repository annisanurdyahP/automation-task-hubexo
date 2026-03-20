from base.basePage import BasePage
from pages.products.productsPage_locator import ProductsPageLocators

class ProductsPage(BasePage):

    def getFirstProductName(self):
        self.wait_until_visible(ProductsPageLocators.TITLE)
        return self.getText(ProductsPageLocators.FIRST_PRODUCT_NAME)

    def addFirstProductToCart(self):
        self.wait_until_visible(ProductsPageLocators.ADD_TO_CART_BUTTON)
        self.clickOnElement(ProductsPageLocators.ADD_TO_CART_BUTTON)

    def goToCart(self):
        self.clickOnElement(ProductsPageLocators.CART_ICON)