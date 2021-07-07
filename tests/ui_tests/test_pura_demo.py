def test_show_pura_my_coding_skills(pura):
    # Go to trypura.com
    pura.py.visit("https://www.trypura.com")
    # Add Pura Smart Device to shopping cart (Pre-order)
    pura.py.get(".Slideshow a[href='/collections/fragrances']").should().be_clickable().click()
    pura.py.get("a[href='/collections/fragrances/products/pura-device-2-0']").scroll_into_view().click(force=True)
    pura.py.get("button[data-action='add-to-cart']").click()
    # assert "Pura Smart Device" in pura.cart.get_list_of_titles_in_cart()
    pura.py.get(".Cart__ItemList a[href*='/products/pura-device-2-0?']").should().be_visible()
    # Remove Pura Smart Device from Cart
    pura.py.get(".CartItem__Actions a[data-action='remove-item']").click(force=True)
    # Verify Pura Smart Device is in Suggested products in Cart
    pura.py.webdriver.find_element_by_link_text("Pura Smart Device").is_displayed()
    # Verify "Pura Smart Device" not in pura cart list
    pura.py.should().not_find(".Cart__ItemList a[href*='/products/pura-device-2-0?']")
    pura.py.should().not_find(".CartItem__Actions a[data-action='remove-item']")
    # Add any available fragrance as one - time purchase
    pura.py.get(".Cart__UpsellList a[href*='maui']").click(force=True)
    pura.py.get("#one_time").click()
    one_time_price = int(pura.py.get("#one_time_price_container").text()[1:])
    pura.py.get("button[data-action='add-to-cart']").click()
    # Add the same fragrance as subscription
    pura.py.get("button[aria-label='Close cart']").click(force=True)
    pura.py.get("#recurring").click()
    recurring_price = float(pura.py.get("#rc_price_autodeliver").text()[1:])
    pura.py.get("button[data-action='add-to-cart']").click()
    sub_total_control = one_time_price + recurring_price
    # Verify the price of fragrance is different in comparison with one - time purchase and subscription
    assert recurring_price < one_time_price
    # Go to Checkout Check the sum is correct
    pura.py.get("#cart-drawer-checkout-button").click(force=True)
    sub_total_actual = float(pura.py.get("#payment_due_amount").text()[1:])
    assert sub_total_control == sub_total_actual
    # Provide email address
    pura.py.get("#checkout_email").type("kodycarling19@testgmail.com")
    # Apply discount code VIP3Z09T7GQ9 - 20 % discount
    pura.py.get("#show-discount-form-link").click()
    pura.py.get("#checkout_discount_code").type("PURASPRING")
    pura.py.get("#apply_discount").click()
    discount_amount = float(format(sub_total_actual*.15, '.2f'))
    pura.py.wait(use_py=True).sleep(2)
    sub_total_control_after_discount_applied = float(pura.py.get("#payment_due_amount").text()[1:])
    # Verify the sum is recalculated correctly
    assert sub_total_control_after_discount_applied == round(sub_total_actual-discount_amount, 2)
    # Do not continue to Checkout, Go back to Cart
    pura.py.get("#continue-button").scroll_into_view()
    pura.py.webdriver.find_element_by_link_text("< Return to cart").click()
    # remove all items from the cart Verify the Cart is empty
    pura.cart.remove_all_items_from_cart()
    assert "Your cart is empty" in pura.py.get(".EmptyState").text()