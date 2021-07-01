

def test_login(login_without_logout, py):

    py.get(".Header__Icon a[href ='/pages/settings']").hover()
    py.get(".DropdownMenu [href='/account/logout']").click()

    assert py.get("#section-header [href= '/account']").is_displayed()


def test_add_something_to_cart(login, py):

    py.getx("//a[text()='Shop']").click()
    py.getx("//button/span[contains(text(),'Pre-order')]").click()

    assert py.get("#cart-drawer-checkout-button").should().be_visible()

    py.get("button[aria-label='Close cart'").click()

