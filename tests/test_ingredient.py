import pytest
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types
from data import INGREDIENT_TEST_DATA


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
    def test_get_price_correct_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
    def test_get_name_correct_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
    def test_get_type_correct_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
