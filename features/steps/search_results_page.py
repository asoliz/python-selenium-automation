from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")


@then('Verify search results are shown for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)
    context.app.search_results_page.verify_product_url(product)


@then('Verify that every product has a name and an image')
def verify_product_name_img(context):
    # To see ALL listings (comment out if you only check top ones)
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(0.5)
    context.driver.execute_script("window.scrollBy(0,1000)", "")

    products = context.driver.find_elements(*LISTINGS)

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(f"🟢: {title}")
        product.find_element(*PRODUCT_IMG)
