from pylenium.driver import Pylenium


class Checkout:
    def __init__(self, py: Pylenium):
        self.py = py

    # Locators
    PAYMENT_DUE_AMOUNT_DIV = "#payment_due_amount"
    EMAIL_INPUT = "#checkout_email"
    DISCOUNT_LINK = "#show-discount-form-link"
    DISCOUNT_INPUT = "#checkout_discount_code"
    DISCOUNT_APPLY_BUTTON = "#apply_discount"
    CONTINUE_BUTTON = "#continue-button"
    RETURN_TO_CART_LINK = "< Return to cart"

    # Actions

    def get_payment_due_amount(self) -> float:
        return float(self.py.get(self.PAYMENT_DUE_AMOUNT_DIV).text()[1:])

    def apply_discount_code(self, code: str, payment_due_before_discount: str):
        self.py.get(self.DISCOUNT_LINK).click()
        self.py.get(self.DISCOUNT_INPUT).type(code)
        self.py.get(self.DISCOUNT_APPLY_BUTTON).click()
        self.py.wait(use_py=True).sleep(2)

    def return_to_cart(self):
        self.py.get(self.CONTINUE_BUTTON).scroll_into_view()
        self.py.webdriver.find_element_by_link_text(self.RETURN_TO_CART_LINK).click()
