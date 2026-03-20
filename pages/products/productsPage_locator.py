from selenium.webdriver.common.by import By


class ProductsPageLocators:
    # @staticmethod
    # def product_container(product_name):
    #     return (
    #         By.XPATH,
    #         f"//div[@data-test='inventory-item-name' and text()='{product_name}']"
    #     )

    # @staticmethod
    # def add_to_cart_inside_product(product_name):
    #     return (
    #         By.XPATH,
    #         f"//div[@data-test='inventory-item-name' and text()='{product_name}']"
    #         f"/ancestor::div[@class='inventory_item']//button[contains(text(),'Add to cart')]"
    #     )
    FIRST_PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    TITLE = (By.XPATH, "//span[@data-test='title']")