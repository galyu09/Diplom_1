import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestBurger:

    @pytest.mark.parametrize('name, price', [('Флюоресцентная булка R2-D3', 988), ('Краторная булка N-200i', 1255)])
    def test_get_bun_name(self, name, price):
        bun = Bun(name, price)
        bun_name = bun.get_name()
        assert bun_name == name

    def test_burger_init(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    @pytest.mark.parametrize('name, price', [('Флюоресцентная булка R2-D3', 555), ('Краторная булка N-200i', 888)])
    def test_set_buns(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize('type, name, price',
                             [
                                 (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 9.0),
                                 (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337.0)
                             ])
    def test_add_ingredient(self, type, name, price):
        burger = Burger()
        ingredient = Ingredient(ingredient_type=type, name=name, price=price)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='Соус Spicy-X', price=9.0)
        ingredient_2 = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,
                                  name='Мясо бессмертных моллюсков Protostomia', price=1337.0)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_2]

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='Соус Spicy-X', price=9.0)
        ingredient_2 = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,
                                  name='Мясо бессмертных моллюсков Protostomia', price=1337.0)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    @pytest.mark.parametrize(
        'ingredients, total_price', [
            (
                [
                    Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='Соус Spicy-X', price=90.0),
                    Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,
                               name='Мясо бессмертных моллюсков Protostomia', price=1337.0)
                ], 3403.0
            ),
            (
                    [
                        Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='Соус с шипами Антарианского плоскоходца', price=88.0),
                        Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,
                                   name='Филе Люминесцентного тетраодонтимформа', price=988.0)
                    ], 3052.0
            )
        ]
    )
    def test_get_price(self, ingredients, total_price):
        burger = Burger()

        burger.set_buns(Bun(name='Флюоресцентная булка R2-D3', price=988))

        burger.ingredients = ingredients

        assert burger.get_price() == total_price

    @pytest.mark.parametrize(
        'ingredients, result_receipt', [
            (
                [
                    Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='Соус Spicy-X', price=90.0),
                    Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,
                               name='Мясо бессмертных моллюсков Protostomia', price=1337.0)
                ],
                "(==== Флюоресцентная булка R2-D3 ====)\n"
                "= sauce Соус Spicy-X =\n"
                "= filling Мясо бессмертных моллюсков Protostomia =\n"
                "(==== Флюоресцентная булка R2-D3 ====)\n\n"
                "Price: 3403.0"
            ),
            (
                [
                 Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name='Соус с шипами Антарианского плоскоходца', price=88.0),
                 Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,
                            name='Биокотлета из марсианской Магнолии', price=424.0)
                ],
                "(==== Флюоресцентная булка R2-D3 ====)\n"
                "= sauce Соус с шипами Антарианского плоскоходца =\n"
                "= filling Биокотлета из марсианской Магнолии =\n"
                "(==== Флюоресцентная булка R2-D3 ====)\n\n"
                "Price: 2488.0"
             )
        ]
    )
    def test_get_receipt(self, ingredients, result_receipt):
        burger = Burger()

        burger.set_buns(Bun(name='Флюоресцентная булка R2-D3', price=988))

        burger.ingredients = ingredients

        assert burger.get_receipt() == result_receipt
