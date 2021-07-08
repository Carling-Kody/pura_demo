from pylenium.driver import Pylenium


class AllFragrances:
    def __init__(self, py: Pylenium):
        self.py = py

    # Locators
    PURA_SMART_DEVICE = "a[href='/collections/fragrances/products/pura-device-2-0']"
    PRE_ORDER_ADD_TO_CART = "button[data-action='add-to-cart']"

    # Actions
