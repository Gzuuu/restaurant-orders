from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    frango = Ingredient("frango")
    coxinha = Dish("coxinha", 4.50)
    coxinha2 = Dish("coxinha", 4.50)
    almondega = Dish("almondega", 3.20)
    expected_restriction = {"ANIMAL_MEAT", "ANIMAL_DERIVED"}

    assert repr(coxinha) == "Dish('coxinha', R$4.50)"
    assert coxinha.name == "coxinha"
    assert not hash(coxinha) == hash(almondega)
    assert hash(coxinha) == hash(coxinha2)
    assert coxinha == coxinha2

    coxinha.add_ingredient_dependency(frango, 1)

    assert coxinha.get_ingredients() == {frango}
    assert (
        set(item.value for item in coxinha.get_restrictions())
        == expected_restriction
    )
    with pytest.raises(TypeError, match="Dish price must be float."):
        coxinha = Dish("coxinha", "4.50")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        coxinha = Dish("churros", 0)
