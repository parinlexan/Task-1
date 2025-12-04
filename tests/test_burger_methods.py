import allure

from praktikum.database import *
from praktikum.burger import *

class TestBurgerMethods:

    @allure.title("Проверяем, что метод set_buns() устанавливает корректные данные")
    def test_set_bun(self, burger_init):
        bun = Bun("TestBulka", 13)
        burger_init.set_buns(bun)

        assert (burger_init.bun.get_name() == bun.name
                and burger_init.bun.get_price() == bun.price)

    @allure.title("Проверяем, что метод add_ingredient() добавляет ингридиент типа заправка")
    def test_add_ingridient_filling(self, burger_init):
        ingr = Ingredient(INGREDIENT_TYPE_FILLING, "TestIngr", 31)
        burger_init.add_ingredient(ingr)

        assert burger_init.ingredients == [ingr]

    @allure.title("Проверяем, что метод add_ingredient() добавляет ингридиент типа соус")
    def test_add_ingridient_sauce(self, burger_init):
        ingr = Ingredient(INGREDIENT_TYPE_SAUCE, "TestIngr", 31)
        burger_init.add_ingredient(ingr)

        assert burger_init.ingredients == [ingr]

    @allure.title("Проверяем, что метод remove_ingredient() удаляет ингридиент")
    def test_remove_ingredient(self, burger_init):
        ingr = Ingredient(INGREDIENT_TYPE_FILLING, "TestIngr", 31)
        ingr1 = Ingredient(INGREDIENT_TYPE_SAUCE, "TestIngr1", 13)
        burger_init.add_ingredient(ingr)
        burger_init.add_ingredient(ingr1)
        burger_init.remove_ingredient(1)

        assert (len(burger_init.ingredients) == 1
                and ingr1 not in burger_init.ingredients
                and ingr in burger_init.ingredients)
    
    @allure.title("Проверяем, что метод remove_ingredient() может удалить единственный ингридиент")
    def test_remove_only_ingredient(self, burger_init):
        ingr = Ingredient(INGREDIENT_TYPE_FILLING, "TestIngr", 31)
        burger_init.add_ingredient(ingr)
        burger_init.remove_ingredient(0)

        assert (len(burger_init.ingredients) == 0
                and ingr not in burger_init.ingredients)
        
    @allure.title("Проверяем, что метод move_ingredient() пермещает ингридиенты в списке")
    def test_move_ingredients(self, burger_init):
        ingr = Ingredient(INGREDIENT_TYPE_FILLING, "TestIngr", 31)
        ingr1 = Ingredient(INGREDIENT_TYPE_FILLING, "TestIngr1", 22)
        ingr2 = Ingredient(INGREDIENT_TYPE_FILLING, "TestIngr2", 11)
        burger_init.add_ingredient(ingr)
        burger_init.add_ingredient(ingr1)
        burger_init.add_ingredient(ingr2)

        assert (burger_init.ingredients == [ingr, ingr1, ingr2])

        burger_init.move_ingredient(0, 2)

        assert (burger_init.ingredients == [ingr1, ingr2, ingr])

    @allure.title("Проверяем, что стоимость бургера расчитывается правильно, price = 400")
    def test_get_price(self, burger_created):
        burger_price = burger_created.get_price()

        assert burger_price == 400

    @allure.title("Проверяем, что чек выводит итоговую сумму (400) и состав бургера:"
                  "black bun, sauce hot sauce, filling cutlet, black bun")
    def test_get_receipt(self, burger_created):
        burger_receipt = burger_created.get_receipt()
        expected_receipt = (
            '(==== black bun ====)\n',
            '= sauce hot sauce =\n',
            '= filling cutlet =\n',
            '(==== black bun ====)\n',
            '\n'
            'Price: 400'
        )

        assert burger_receipt == ''.join(expected_receipt)