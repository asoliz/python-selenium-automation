from behave import given, when, then
from selenium.webdriver.common.by import By

COLOR_OPTIONS = (By.CSS_SELECTOR, 'li[class*="CarouselItem"] img')
SELECTED_COLOR = (By.XPATH, '//div[@data-test="@web/VariationComponent"]')


@given('Open target product A-54083344')
def open_main(context):
    context.driver.get(
        'https://www.target.com/p/women-s-bliss-lightly-lined-wirefree-bra-auden-153/-/A-54083344')


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Brown', 'Soft Beige', 'Sandbank Brown', 'Moss Green']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for c in colors:
        c.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text

        selected_color = selected_color.split('\n')[1]
        print('Selected color:', selected_color)
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f"Expected {expected_colors} did not mach actual {actual_colors}"
