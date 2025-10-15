from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART = (By.XPATH, '//div[@data-test="boxEmptyMsg"]')

    def verify_empty_cart_message(self):
        expected_cart_text = "Your cart is empty"
        actual_cart_text = self.driver.find_element(*self.EMPTY_CART).text
        assert expected_cart_text == actual_cart_text, f"Error: Expected text {expected_cart_text} but got {actual_cart_text}"
