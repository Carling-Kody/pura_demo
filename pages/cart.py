from pylenium.driver import Pylenium
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException


class Cart:
    def __init__(self, py: Pylenium):
        self.py = py

    # Locators
    CART_REMOVE_ITEM_LINK = "form[method='post'] > div > div:nth-of-type(2)" \
                                " > .CartItem__Actions.Heading.Text--subdued > .CartItem__Remove.Link"
    # Actions

    def get_list_of_titles_in_suggested_area_of_cart(self):
        text_suggested_products = self.py.get('.Cart__UpsellList a').text()
        suggested_products_list = text_suggested_products.split('\n')
        return suggested_products_list

    def remove_all_items_from_cart(self):
        self.py.get(self.CART_REMOVE_ITEM_LINK).click(force=True)
        self.py.wait(use_py=True).sleep(1)
        self.py.get(self.CART_REMOVE_ITEM_LINK).click(
            force=True)
