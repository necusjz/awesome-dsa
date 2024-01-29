from src.design_patterns.builder import BurgerBuilder


def test_builder():
    BurgerBuilder()\
        .add_buns("sesame")\
        .add_patty("fish-patty")\
        .add_cheese("swiss-cheese")\
        .build()
