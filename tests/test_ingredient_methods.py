import pytest
import allure

from praktikum.database import *


class TestDatabaseMethods:

    @allure.title("Проверяем, что метод get_name() отдает верное название ингридиента для типа соус")
    @pytest.mark.parametrize("type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                              (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                              (INGREDIENT_TYPE_SAUCE, "chili cream", 300)])
    def test_db_buns_available_ingr_sauce_names(self, database_init, type, name, price):
        ingridient = Ingredient(type, name, price)
        assert ingridient.get_name() == name

    @allure.title("Проверяем, что метод get_price() отдает верную цену ингридиента для типа соус")
    @pytest.mark.parametrize("type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                              (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                              (INGREDIENT_TYPE_SAUCE, "chili cream", 300)])
    def test_db_buns_available_ingr_sauce_prices(self, database_init, type, name, price):
        ingridient = Ingredient(type, name, price)
        assert ingridient.get_price() == price

    @allure.title("Проверяем, что метод get_type() отдает верный тип ингридиента")
    @pytest.mark.parametrize("type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                              (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                              (INGREDIENT_TYPE_SAUCE, "chili cream", 300),
                              (INGREDIENT_TYPE_FILLING, "cutlet", 100),
                              (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                              (INGREDIENT_TYPE_FILLING, "sausage", 300)
                              ])
    def test_db_buns_available_ingr_types(self, database_init, type, name, price):
        ingridient = Ingredient(type, name, price)
        assert ingridient.get_type() == type

    @allure.title("Проверяем, что метод get_price() отдает верную цену ингридиента для типа заправка")
    @pytest.mark.parametrize("type, name, price",
                             [(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                              (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                              (INGREDIENT_TYPE_FILLING, "sausage", 300)])
    def test_db_buns_available_ingr_filling_prices(self, database_init, type, name, price):
        ingridient = Ingredient(type, name, price)
        assert ingridient.get_price() == price

    @allure.title("Проверяем, что метод get_name() отдает верное название ингридиента для типа заправка")
    @pytest.mark.parametrize("type, name, price",
                             [(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                              (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                              (INGREDIENT_TYPE_FILLING, "sausage", 300)])
    def test_db_buns_available_ingr_filling_names(self, database_init, type, name, price):
        ingridient = Ingredient(type, name, price)
        assert ingridient.get_name() == name