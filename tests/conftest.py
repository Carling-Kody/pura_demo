import pytest
from pages.pura_page_wrapper import PuraPages


@pytest.fixture()
def pura(py) -> PuraPages:
    return PuraPages(py)