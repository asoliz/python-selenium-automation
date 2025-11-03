from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class TargetReturnsPage(Page):
    HELP_TOPICS = (By.XPATH, '//select[contains(@id, "ViewHelpTopics")]')
    RETURNS_HEADER = (By.XPATH, '//h1[text()= " Returns"]')
    HELP_TOPIC_HEADER = (By.ID, 'pageTitle')

    def open_help_returns_page(self):
        self.driver.get('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_helptopics_dropdown(self, help_topic):
        dropdown_menu = self.find_element(*self.HELP_TOPICS)
        select = Select(dropdown_menu)
        select.select_by_value(help_topic)

    def verify_returns_header(self):
        self.find_element(*self.RETURNS_HEADER)

    def verify_header_help_topic(self, help_topic_header):
        header = self.find_element(*self.HELP_TOPIC_HEADER).text
        assert header == help_topic_header, f"{header} != {help_topic_header}"
