from pages.login.loginPage import LoginPage
from pages.products.productsPage import ProductsPage
from pages.cart.cartPage import CartPage
import time


class TestCart:

    def test_add_product_to_cart(self, driver):
        lp = LoginPage(driver)
        pp = ProductsPage(driver)
        cp = CartPage(driver)
        lp.open()
        lp.inputLogin("standard_user", "secret_sauce")
        product_name = pp.getFirstProductName()
        pp.addFirstProductToCart()
        pp.goToCart()
        assert cp.getProductName() == product_name
        assert cp.getProductQuantity() == "1"
        # time.sleep(10000)