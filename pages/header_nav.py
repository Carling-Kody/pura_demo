from pylenium.driver import Pylenium


class HeaderNav:
    def __init__(self, py: Pylenium):
        self.py = py

    # Locators

    # Actions
    def get_list_of_titles_in_cart(self):
        titles = []
        elements = self.py.find('.CartItem__Info')
        for element in elements:
            titles.append(element)
        return titles