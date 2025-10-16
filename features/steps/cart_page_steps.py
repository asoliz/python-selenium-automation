from behave import when, then


@then('Verify empty cart message appears')
def verify_empty_cart_message(context):
    context.app.cart_page.verify_empty_cart_message()


@when('Click Add to cart on first product in search results')
def first_product_is_added(context):
    context.app.cart_page.add_first_product()


@when('Click Add to cart from side navigation')
def confirm_is_added(context):
    context.app.side_navigation.add_to_cart_confirmation()
    context.app.side_navigation.close_sidebar()


@then('Verify {product_name} is added to cart')
def verify_product_name(context, product_name):
    context.app.cart_page.verify_product_in_cart(product_name)
