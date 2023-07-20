from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("salmão")
    ingredient3 = Ingredient("bacon")
    expected_restriction = {"ANIMAL_MEAT", "ANIMAL_DERIVED"}

    assert not ingredient1 == ingredient2
    assert ingredient1 == ingredient3
    assert not hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) == hash(ingredient3)
    assert ingredient1.name == "bacon"
    assert repr(ingredient1) == "Ingredient('bacon')"
    assert (
        set(item.value for item in ingredient1.restrictions)
        == expected_restriction
    )
