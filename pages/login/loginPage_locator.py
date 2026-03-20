from selenium.webdriver.common.by import By


class LoginPageLocators:

  userNameField = (By.ID, "user-name")
  passwordField = (By.ID, "password")
  loginButton = (By.ID, "login-button")
  ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
  burgerMenuButton = (By.ID, "react-burger-menu-btn")
  logoutButton = (By.ID, "logout_sidebar_link")