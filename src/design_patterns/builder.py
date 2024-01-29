class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None

    def set_buns(self, bun_style):
        self.buns = bun_style

    def set_patty(self, patty_style):
        self.patty = patty_style

    def set_cheese(self, cheese_style):
        self.cheese = cheese_style


class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_buns(self, bun_style):
        self.burger.set_buns(bun_style)

        return self

    def add_patty(self, patty_style):
        self.burger.set_patty(patty_style)

        return self

    def add_cheese(self, cheese_style):
        self.burger.set_cheese(cheese_style)

        return self

    def build(self):
        return self.burger
