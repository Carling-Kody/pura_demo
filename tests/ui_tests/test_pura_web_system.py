

def test_login(login_without_logout, py):

    py.get(".Header__Icon a[href ='/pages/settings']").hover()
    py.get(".DropdownMenu [href='/account/logout']").click()

    assert py.get("#section-header [href= '/account']").is_displayed()
