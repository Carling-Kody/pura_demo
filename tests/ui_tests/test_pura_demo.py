def test_show_pura_my_coding_skills(pura):
    # Go to trypura.com
    pura.py.visit("https://www.trypura.com")
    # Add Pura Smart Device to shopping cart (Pre-order)
    pura.py.get(".Slideshow a[href='/collections/fragrances']").should().be_clickable().click()
    pura.py.get("a[href='/collections/fragrances/products/pura-device-2-0']").scroll_into_view().click(force=True)
    pura.py.get("button[data-action='add-to-cart']").click()
    '''Verify Pura Smart Device is not in Suggested products in Cart
    assert "Pura Smart Device" not in pura.cart.get_list_of_titles_in_suggested_area_of_cart()'''
    # assert "Pura Smart Device" in pura.cart.get_list_of_titles_in_cart()
    # Remove Pura Smart Device from Cart
    pura.py.get(".CartItem__Actions a[data-action='remove-item']").click(force=True)
    # Verify Pura Smart Device is in Suggested products in Cart
    '''assert "Pura Smart Device" in pura.cart.get_list_of_titles_in_suggested_area_of_cart()
    # assert "Pura Smart Device" not in pura.cart.get_list_of_titles_in_suggested_area_of_cart()'''
    # Add any available fragrance as one - time purchase
    pura.py.get(".Cart__UpsellList a[href*='maui']").click(force=True)
    pura.py.get("#one_time").click()
    pura.py.get("button[data-action='add-to-cart']").click()
    # Add the same fragrance as subscription
    pura.py.get("button[aria-label='Close cart']").click()
    pura.py.get("#recurring").click()
    pura.py.get("button[data-action='add-to-cart']").click()
    pura.py.wait(use_py=True).sleep(10)
    # Verify the price of fragrance is different in comparison with one - time purchase and subscription
    # Go to Checkout Check the sum is correct
    # Provide email address
    # Apply discount code VIP 3Z09T7GQ9 - 20 % discount
    # Verify the sum is recalculated correctly
    # Do not continue to Checkout, Go back to Cart and remove all items from the cart Verify the Cart is empty
