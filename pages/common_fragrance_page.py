from pylenium.driver import Pylenium


class CommonFragrancePage:
    def __init__(self, py: Pylenium):
        self.py = py

    # Locators
    ONE_TIME_PURCHASE_TOGGLE = "#one_time"
    RECURRING_PURCHASE_TOGGLE = "#recurring"
    ONE_TIME_PURCHASE_PRICE_CONTAINER = "#one_time_price_container"
    RECURRING_PURCHASE_PRICE_CONTAINER = "#rc_price_autodeliver"
    ADD_TO_CART_BUTTON = "button[data-action='add-to-cart']"

    # Actions

    def get_one_time_purchase_price(self) -> int:
        """ grabs the text from the one time purchase price div
                 and then strips off the $ sign and converts the string to an integer """
        return int(self.py.get(self.ONE_TIME_PURCHASE_PRICE_CONTAINER).text()[1:])

    def get_recurring_purchase_price(self) -> float:
        """ grabs the text from the recurring price div
                         and then strips off the $ sign and converts the string to a float """
        return float(self.py.get(self.RECURRING_PURCHASE_PRICE_CONTAINER).text()[1:])
