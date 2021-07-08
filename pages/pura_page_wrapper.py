from pylenium.driver import Pylenium

from pages.all_fragrances import AllFragrances
from pages.checkout import Checkout
from pages.common_fragrance_page import CommonFragrancePage
from pages.header_nav import HeaderNav
from pages.cart import Cart
from pages.home import HomePage


class PuraPages:
    def __init__(self, py: Pylenium):
        self.py = py
        self.header_nav = HeaderNav(py)
        self.cart = Cart(py)
        self.home = HomePage(py)
        self.all_fragrances = AllFragrances(py)
        self.common_fragrance_page = CommonFragrancePage(py)
        self.checkout = Checkout(py)