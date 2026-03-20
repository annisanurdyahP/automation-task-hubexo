from pages.login.loginPage import LoginPage


class TestLogin:

    def test_login(self, driver):
        lp = LoginPage(driver)

        users = [
            {
                "username": "standard_user",
                "password": "secret_sauce",
                "expected": "success"
            },
            {
                "username": "locked_out_user",
                "password": "secret_sauce",
                "expected": "error",
                "message": "Epic sadface: Sorry, this user has been locked out."
            },
            {
                "username": "",
                "password": "wrong_password",
                "expected": "error",
                "message": "Epic sadface: Username is required"
            },
            {
                "username": "problem_user",
                "password": "wrong_password",
                "expected": "error",
                "message": "Epic sadface: Username and password do not match any user in this service"
            },
            {
                "username": "performance_glitch_user",
                "password": "secret_sauce",
                "expected": "success"
            },
            {
                "username": "error_user",
                "password": "secret_sauce",
                "expected": "success",
            },
            {
                "username": "visual_user",
                "password": "secret_sauce",
                "expected": "success",
            },
        ]

        for user in users:
            lp.open()
            lp.inputLogin(user["username"], user["password"])
            if user["expected"] == "success":
                assert driver.current_url == "https://www.saucedemo.com/inventory.html"
                lp.clickLogout()
                lp.verifyLogoutSuccessful()
            else:
                error_message = lp.getErrorMessage()
                assert error_message == user["message"]