from src.design_patterns.factory_method import BurgerFactory


def test_factory_method():
    factory = BurgerFactory()

    assert factory.create_cheese_burger().ingredients == ["bun", "cheese", "beef-patty"]
    assert factory.create_deluxe_cheese_burger().ingredients == ["bun", "tomato", "lettuce", "cheese", "beef-patty"]
    assert factory.create_vegan_burger().ingredients == ["bun", "special-sauce", "veggie-patty"]
