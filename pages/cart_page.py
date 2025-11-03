from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART = (By.XPATH, '//div[@data-test="boxEmptyMsg"]')
    SEARCH_RESULTS = (By.XPATH, '//div[@data-test="lp-resultsCount"]')
    ADD_TO_CART = (By.XPATH, '//button[@data-test="chooseOptionsButton"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')

    def verify_empty_cart_message(self):
        self.verify_text("Your cart is empty", *self.EMPTY_CART)

    def add_first_product(self):
        self.wait_until_element_appears(*self.SEARCH_RESULTS)
        self.wait_until_clickable_then_click(*self.ADD_TO_CART)

    def verify_product_in_cart(self, product_name):
        self.verify_partial_text(product_name, *self.PRODUCT_NAME)
        # actual_result = context.driver.find_element(*PRODUCT_NAME).text
        # assert product_name in actual_result.lower(), f"Error: Expected {product_name} but got {actual_result}"

    def verify_cart_page_opened(self):
        self.wait_until_url_contains('/cart')

