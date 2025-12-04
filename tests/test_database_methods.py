import allure


class TestDatabaseMethods:

    @allure.title("Проверяем, что количество доступных булочек в бд = 3")
    def test_db_buns_amount(self, database_init):
        bun_list = database_init.available_buns()
        assert len(bun_list) == 3

    @allure.title("Проверяем, что количество доступных ингридиентов в бд = 6")
    def test_db_ingredients_amount(self, database_init):
        ingredient_list = database_init.available_ingredients()
        assert len(ingredient_list) == 6

    @allure.title("Проверяем, что тип ингридиента определяется корректно в зависимости от названия")
    def test_db_buns_available_ingr_types(self, database_init):
        ingridients_list = database_init.available_ingredients()
        for i in ingridients_list:
            if i.name == i.name:
                assert i.type == i.type

    @allure.title("Проверяем, что у каждой булочки своя цена")
    def test_db_buns_available_bun_prices(self, database_init):
        bun_list = database_init.available_buns()
        for bun in bun_list:
            if bun.name == bun.name:
                assert bun.price == bun.price

    @allure.title("Проверяем, что у каждого ингридиента своя цена")
    def test_db_buns_available_ingr_prices_types(self, database_init):
        ingridient_list = database_init.available_ingredients()
        for i in ingridient_list:
            if i.name == i.name:
                assert i.price == i.price
