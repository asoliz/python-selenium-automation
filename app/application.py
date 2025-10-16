from pages.base_page import Page
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.header import Header
from pages.side_navigation import SideNavigation
from pages.signin_page import SignInPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.signin_page = SignInPage(driver)
        self.circle_page = CirclePage(driver)
        self.side_navigation = SideNavigation(driver)
