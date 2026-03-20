from pages.login.loginPage import LoginPage
from pages.products.productsPage import ProductsPage
from pages.cart.cartPage import CartPage
from pages.checkout.checkoutPage import CheckoutPage


class TestCheckout:

    def test_checkout_flow(self, driver):
        lp = LoginPage(driver)
        pp = ProductsPage(driver)
        cp = CartPage(driver)
        checkout = CheckoutPage(driver)

        lp.open()
        lp.inputLogin("standard_user", "secret_sauce")
        product_name = pp.getFirstProductName()
        pp.addFirstProductToCart()
        pp.goToCart()
        assert cp.getProductName() == product_name
        assert cp.getProductQuantity() == "1"
        checkout.clickCheckout()
        checkout.fillInformation()
        checkout.clickContinue()
        checkout.clickFinish()
        assert checkout.getSuccessMessage() == "Thank you for your order!"
        checkout.clickBackHome()
        assert "inventory" in driver.current_url