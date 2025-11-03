from pages.base_page import Page
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.header import Header
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.side_navigation import SideNavigation
from pages.signin_page import SignInPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.target_app_page import TargetAppPage
from pages.target_returns_page import TargetReturnsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        # self.base_page = Page(driver)
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.signin_page = SignInPage(driver)
        self.circle_page = CirclePage(driver)
        self.side_navigation = SideNavigation(driver)
        self.target_app_page = TargetAppPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.target_returns_page = TargetReturnsPage(driver)
