from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page


class CirclePage(Page):
    BENEFIT_CARDS = (By.CSS_SELECTOR, '[class="cell-item-content"]')

    # def navigate_to_circle_page
    pass
