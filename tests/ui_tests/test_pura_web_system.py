

def test_login(login, py):

    py.get(".Header__Icon a[href ='/pages/settings']").hover()
    py.get(".DropdownMenu [href='/account/logout']").click()

    assert py.get("#section-header [href= '/account']").is_displayed()


def test_add_smart_device_to_cart(login, py):

    py.getx("//a[text()='Shop']").click()
    py.getx("//button/span[contains(text(),'Pre-order')]").click()

    assert py.get("#cart-drawer-checkout-button").should().be_visible()

    # py.get("button[aria-label='Close cart']").click(force=True)


def test_add_volcano_fragrance_from_best_sellers_to_cart(login, pura):

    pura.py.getx("//a[text()='Shop']").hover()
    pura.py.get("[href='/collections/best-sellers']").click()
    pura.py.get(".ProductItem__Title a[href*='volcano']").scroll_into_view().click(force=True)
    pura.py.get("#one_time").click()
    pura.py.get("button[data-action='add-to-cart']").click()

    assert "volcano" in pura.header_nav.get_list_of_titles_in_suggested_area_of_cart()

