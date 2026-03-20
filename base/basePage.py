from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickOnElement(self, locator):
        element = self.wait_until_visible(locator)
        element.click()

    def sendText(self, locator, text):
        element = self.wait_until_visible(locator)
        element.send_keys(text)

    def clearFieldText(self, locator):
        element = self.wait_until_visible(locator)
        element.clear()


    def getText(self, locator):
        element = self.wait_until_visible(locator)
        return element.text