from pylenium.driver import Pylenium
from pages.header_nav import HeaderNav
from pages.cart import Cart


class PuraPages:
    def __init__(self, py: Pylenium):
        self.py = py
        self.header_nav = HeaderNav(py)
        self.cart = Cart(py)