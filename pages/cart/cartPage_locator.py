from selenium.webdriver.common.by import By


class CartPageLocators:
    PRODUCT_NAME_CART = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_QTY = (By.CLASS_NAME, "cart_quantity")