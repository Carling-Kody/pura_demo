from pylenium.driver import Pylenium


class HomePage:
    def __init__(self, py: Pylenium):
        self.py = py

    # Locators
    SHOP_BUTTON = ".Slideshow a[href='/collections/fragrances']"

    # Actions
