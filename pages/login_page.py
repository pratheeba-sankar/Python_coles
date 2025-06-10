import time


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_btn = page.get_by_text("Log in / Sign up")
        self.username_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.continue_button = page.locator("//*[@id='email-validator-continue']/span")
        self.existing_user_login = page.locator("#existing-user-login")

    def login(self, username, password):
        try:
            print("I m here")
            time.sleep(10)
            #self.login.wait_for(state="visible")
            self.login_btn.hover()
            self.login_btn.click()
            self.username_input.click()
            self.username_input.fill(username)
            time.sleep(5)
            self.continue_button.click()
            time.sleep(5)
            self.password_input.fill(password)
            self.existing_user_login.click()
        except Exception as e:
            raise Exception(f"Login failed due to: {str(e)}")