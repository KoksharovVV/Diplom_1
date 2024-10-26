import pytest
from data import TestData
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        "name,price", [("Имя", 123.4), ("Имя1", 123.4), ("имя", 123.4), ("name", 123.4), ("", 123.4)])
    def test_name_of_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name

    @pytest.mark.parametrize(
        "name,price", [("Имя", 123.4), ("Имя", 123), ("Имя", 12333333), ("Имя", 0), ("Имя", -1)])
    def test_price_of_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.price == price

    @pytest.mark.parametrize(
        "name", ["Имя", "Имя1", "имя", "name", "", None])
    def test_get_name_true_name(self, name):
        bun = Bun(name, TestData.BUN_PRICE)
        assert bun.get_name() == name

    def test_get_name_return_str(self):
        bun = Bun(TestData.BUN_NAME, TestData.BUN_PRICE)
        name_result = bun.get_name()
        assert isinstance(name_result, str)

    @pytest.mark.parametrize(
        "price", [120.7, 120, 120000000000000, 0, -1])
    def test_get_price_true_price(self, price):
        bun = Bun(TestData.BUN_NAME, price)
        assert bun.get_price() == price

    def test_get_price_true_return_float(self):
        bun = Bun(TestData.BUN_NAME, TestData.BUN_PRICE)
        name_result = bun.get_price()
        assert isinstance(name_result, float)
