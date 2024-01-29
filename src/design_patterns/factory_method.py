class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients


class BurgerFactory:
    @staticmethod
    def create_cheese_burger():
        ingredients = ["bun", "cheese", "beef-patty"]

        return Burger(ingredients)

    @staticmethod
    def create_deluxe_cheese_burger():
        ingredients = ["bun", "tomato", "lettuce", "cheese", "beef-patty"]

        return Burger(ingredients)

    @staticmethod
    def create_vegan_burger():
        ingredients = ["bun", "special-sauce", "veggie-patty"]

        return Burger(ingredients)
