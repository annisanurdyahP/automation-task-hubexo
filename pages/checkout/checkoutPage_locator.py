from selenium.webdriver.common.by import By


class CheckoutPageLocators:

    # step 1
    CHECKOUT_BUTTON = (By.ID, "checkout")

    # form
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")

    # step 2
    FINISH_BUTTON = (By.ID, "finish")

    # success page
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")