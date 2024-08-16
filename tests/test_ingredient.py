import pytest
from data import TestData
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize(
        "types", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_types_of_ingredient(self, types):
        ingredient = Ingredient(types, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE)
        assert ingredient.type == types

    def test_types_of_ingredient_is_str(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.type, str)

    @pytest.mark.parametrize(
        "name", ["Имя", "Имя1", "имя", "name", "", None])
    def test_name_of_ingredient(self, name):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, name, TestData.INGREDIENT_PRICE)
        assert ingredient.name == name

    def test_name_of_ingredient_is_str(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.name, str)

    @pytest.mark.parametrize(
        "price", [123.4, 123, 123400000000000, 0, -1])
    def test_prices_of_ingredient(self, price):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, price)
        assert ingredient.price == price

    def test_price_of_ingredient_is_float(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.price, float)

    @pytest.mark.parametrize(
        "types", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_true_type(self, types):
        ingredient = Ingredient(types, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE)
        assert ingredient.get_type() == types

    def test_get_type_true_return_str(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.get_type(), str)

    @pytest.mark.parametrize(
        "name", ["Имя", "Имя1", "имя", "name", "", None])
    def test_get_name_true_name(self, name):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, name, TestData.INGREDIENT_PRICE)
        assert ingredient.get_name() == name

    def test_get_name_return_is_str(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.get_name(), str)

    @pytest.mark.parametrize(
        "price", [120.7, 120, 120000000000000, 0, -1])
    def test_get_price_true_price(self, price):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, price)
        assert ingredient.get_price() == price

    def test_get_price_return_is_float(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.get_price(), float)
