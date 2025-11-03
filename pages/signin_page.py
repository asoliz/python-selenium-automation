from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):

    SIGNIN_TEXT = (By.XPATH, "//*[text()='Sign in or create account']")
    SIGNIN_BUTTON = (By.XPATH, "//button[normalize-space()='Sign in with passkey']")
    EMAIL_FIELD = (By.ID, "username")
    CONTINUE_BUTTON = (By.ID, "login")
    ENTER_PASSWORD_BUTTON = (By.ID, "password")
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-test="login-password"]')
    PASSWORD_SUBMIT_BUTTON = (By.XPATH, '//button[text()="Sign in with password"]')
    TOC_LINK = (By.XPATH, '//a[@aria-label="terms & conditions - opens in a new window"]')

    def verify_sign_in_text(self):
        self.verify_text("Sign in or create account", *self.SIGNIN_TEXT)

    def verify_sign_in_button(self):
        self.verify_element_exists(*self.SIGNIN_BUTTON)

    def enter_email_then_submit(self, email):
        self.input_text(email, *self.EMAIL_FIELD)
        self.wait_until_clickable_then_click(*self.CONTINUE_BUTTON)

    def enter_password_then_submit(self, password):
        self.wait_until_clickable_then_click(*self.ENTER_PASSWORD_BUTTON)
        self.wait_until_element_appears(*self.PASSWORD_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.wait_until_clickable_then_click(*self.PASSWORD_SUBMIT_BUTTON)

    def sign_in_successful(self):
        self.wait_until_element_disappears(*self.PASSWORD_SUBMIT_BUTTON)

    def verify_signin_opened(self):
        self.wait_until_url_contains('/login')

    def open_signin_page(self):
        self.open_url('https://www.target.com/')



