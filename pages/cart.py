from pylenium.driver import Pylenium
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException


class Cart:
    def __init__(self, py: Pylenium):
        self.py = py

    # Locators
    CLOSE_CART_BUTTON = "button[aria-label='Close cart']"
    PURA_SMART_DEVICE_IN_CART_LIST = ".Cart__ItemList a[href*='/products/pura-device-2-0?']"
    FIRST_REMOVE_ITEM_LINK_IN_CART_LIST = ".CartItem__Actions a[data-action='remove-item']"
    CART_REMOVE_ITEM_LINK = "form[method='post'] > div > div:nth-of-type(2)> .CartItem__Actions.Heading.Text--subdued > .CartItem__Remove.Link"
    MAUI_MANGO_SUGGESTED_PRODUCT_LIST_LINK = ".Cart__UpsellList a[href*='maui']"
    CART_CHECKOUT_BUTTON = "#cart-drawer-checkout-button"

    # Actions

    @staticmethod
    def calculate_sub_total(items: list) -> float:
        total = 0
        for item in range(0, len(items)):
            total = total + items[item]
        return total

    def remove_all_items_from_cart(self):
        self.py.get(self.CART_REMOVE_ITEM_LINK).click(force=True)
        self.py.wait(use_py=True).sleep(1)
        self.py.get(self.CART_REMOVE_ITEM_LINK).click(
            force=True)
