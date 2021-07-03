from pylenium.driver import Pylenium


class Cart:
    def __init__(self, py: Pylenium):
        self.py = py

        # Locators

        # Actions

    def get_list_of_titles_in_suggested_area_of_cart(self):
        text_suggested_products = self.py.get('.Cart__UpsellList a').text()
        suggested_products_list = text_suggested_products.split('\n')
        return suggested_products_list