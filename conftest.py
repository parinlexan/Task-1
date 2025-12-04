import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def database_init():
    db = Database()
    return db

@pytest.fixture
def burger_init():
    burger = Burger()
    return burger

@pytest.fixture
def burger_created(burger_init):
    mock_db = Mock()
    bun = Bun("black bun", 100)
    ingr1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    ingr2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    mock_db.available_buns().return_value = [bun]
    mock_db.available_ingredients().return_value = [ingr1, ingr2]
    burger_init.set_buns(bun)
    burger_init.add_ingredient(ingr1)
    burger_init.add_ingredient(ingr2)
    return burger_init