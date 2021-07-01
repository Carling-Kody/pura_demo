from pylenium.driver import Pylenium
from pages.header_nav import HeaderNav


class PuraPages:
    def __init__(self, py: Pylenium):
        self.header_nav = HeaderNav(py)