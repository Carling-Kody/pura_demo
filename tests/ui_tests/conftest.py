import pytest


@pytest.fixture()
def login(py):
    py.visit("https://www.trypura.com")
    py.get("#section-header [href= '/account']").click()
    py.get("#loginEmail").type("kodycarling19@gmail.com")
    py.get("#loginPassword").type("Sm00ch*8")
    py.get("#btnLogin").click()

    # yield
    #
    # py.get(".Header__Icon a[href ='/pages/settings']").hover()
    # py.get(".DropdownMenu [href='/account/logout']").click()



