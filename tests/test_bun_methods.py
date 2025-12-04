import pytest
import allure

from praktikum.database import *

class TestBunMethods:

    @allure.title("Проверяем, что get_name() отдает верное название")
    @pytest.mark.parametrize("name, price",
                             [("black bun", 100),
                              ("white bun", 200),
                              ("red bun", 300)])
    def test_get_name_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @allure.title("Проверяем, что get_price() отдает верную цену")
    @pytest.mark.parametrize("name, price",
                             [("black bun", 100),
                              ("white bun", 200),
                              ("red bun", 300)])
    def test_get_name_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price