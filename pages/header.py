from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
    ACCOUNT_BUTTON = (By.ID, "account-sign-in")
    SIGNIN_BUTTON = (By.XPATH, "//*[@data-test='accountNav-signIn']")

    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(9)

    def click_cart_icon(self):
        self.wait_until_clickable_then_click(*self.CART_ICON)

    def click_account_button(self):
        self.click(*self.ACCOUNT_BUTTON)
