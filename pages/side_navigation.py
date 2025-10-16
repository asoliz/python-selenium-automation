from selenium.webdriver.common.by import By

from pages.base_page import Page


class SideNavigation(Page):
    SIGNIN_BUTTON = (By.XPATH, "//*[@data-test='accountNav-signIn']")
    CONFIRM_TO_CART = (By.XPATH, '//button[@data-test="shippingButton"]')
    CLOSE_DRAWER = (By.CSS_SELECTOR, '[aria-label="close"]')

    def click_signin_button(self):
        self.click(*self.SIGNIN_BUTTON)

    def add_to_cart_confirmation(self):
        self.wait_until_clickable_then_click(*self.CONFIRM_TO_CART)

    def close_sidebar(self):
        self.wait_until_clickable_then_click(*self.CLOSE_DRAWER)
