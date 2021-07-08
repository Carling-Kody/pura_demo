def test_show_pura_my_coding_skills(pura):
    test_email_address = "kodycarling19@testgmail.com"
    test_discount_code = "PURASPRING"
    # Go to trypura.com
    pura.py.visit("https://www.trypura.com")
    # Add Pura Smart Device to shopping cart (Pre-order)
    pura.py.get(pura.home.SHOP_BUTTON).should().be_clickable().click()
    pura.py.get(pura.all_fragrances.PURA_SMART_DEVICE).scroll_into_view().click(force=True)
    pura.py.get(pura.all_fragrances.PRE_ORDER_ADD_TO_CART).click()
    # assert "Pura Smart Device" in pura.cart.get_list_of_titles_in_cart()
    pura.py.get(pura.cart.PURA_SMART_DEVICE_IN_CART_LIST).should().be_visible()
    # Remove Pura Smart Device from Cart
    pura.py.get(pura.cart.FIRST_REMOVE_ITEM_LINK_IN_CART_LIST).click(force=True)
    # Verify Pura Smart Device is in Suggested products in Cart
    pura.py.webdriver.find_element_by_link_text("Pura Smart Device").is_displayed()
    # Verify "Pura Smart Device" not in pura cart list
    pura.py.should().not_find(pura.cart.PURA_SMART_DEVICE_IN_CART_LIST)
    pura.py.should().not_find(pura.cart.FIRST_REMOVE_ITEM_LINK_IN_CART_LIST)
    # Add any available fragrance as one - time purchase
    pura.py.get(pura.cart.MAUI_MANGO_SUGGESTED_PRODUCT_LIST_LINK).click(force=True)
    pura.py.get(pura.common_fragrance_page.ONE_TIME_PURCHASE_TOGGLE).click()
    one_time_price = pura.common_fragrance_page.get_one_time_purchase_price()
    pura.py.get(pura.common_fragrance_page.ADD_TO_CART_BUTTON).click()
    # Add the same fragrance as subscription
    pura.py.get(pura.cart.CLOSE_CART_BUTTON).click(force=True)
    pura.py.get(pura.common_fragrance_page.RECURRING_PURCHASE_TOGGLE).click()
    recurring_price = pura.common_fragrance_page.get_recurring_purchase_price()
    pura.py.get(pura.common_fragrance_page.ADD_TO_CART_BUTTON).click()
    sub_total_calculated = pura.cart.calculate_sub_total([one_time_price, recurring_price])
    # Verify the price of fragrance is different in comparison with one - time purchase and subscription
    assert recurring_price < one_time_price
    # Go to Checkout Check the sum is correct
    pura.py.get(pura.cart.CART_CHECKOUT_BUTTON).click(force=True)
    payment_amount_due = pura.checkout.get_payment_due_amount()
    assert sub_total_calculated == payment_amount_due
    # Provide email address
    pura.py.get(pura.checkout.EMAIL_INPUT).type(test_email_address)
    # Apply discount code VIP3Z09T7GQ9 - 20 % disc I used "PURASPRING" because the code I was given would not work
    pura.checkout.apply_discount_code(test_discount_code, payment_amount_due)
    discount_amount = float(format(payment_amount_due*.15, '.2f'))
    payment_due_after_discount_applied = pura.checkout.get_payment_due_amount()
    # Verify the sum is recalculated correctly
    assert payment_due_after_discount_applied == round(payment_amount_due-discount_amount, 2)
    # Do not continue to Checkout, Go back to Cart
    pura.checkout.return_to_cart()
    # remove all items from the cart Verify the Cart is empty
    pura.cart.remove_two_items_from_cart()
    assert "Your cart is empty" in pura.py.get(".EmptyState").text()
