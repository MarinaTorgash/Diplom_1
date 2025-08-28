import pytest
from praktikum.bun import Bun
from data import BUN_DATA


class TestBun:

    @pytest.mark.parametrize("name, price", BUN_DATA)
    def test_get_correct_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", BUN_DATA)
    def test_get_correct_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
