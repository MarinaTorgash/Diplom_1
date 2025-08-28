
BUN_DATA = [
    ("Булочка", 10.0),
    ("Булочка с кунжутом", 12.5),
    ("Черная булочка", 13.75),
]
EXPECTED_BUNS = [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300),
]

EXPECTED_SAUCES = [
    ("hot sauce", 100),
    ("sour cream", 200),
    ("chili sauce", 300),
]
EXPECTED_FILLINGS = [
    ("cutlet", 100),
    ("dinosaur", 200),
    ("sausage", 300),
]

MOCK_BUN_NAME = "Булочка"
MOCK_BUN_PRICE = 10.0

MOCK_INGREDIENT_NAME = "Соус"
MOCK_INGREDIENT_TYPE = "SAUCE"
MOCK_INGREDIENT_PRICE = 5.0

SECOND_INGREDIENT_NAME = "Сыр"
SECOND_INGREDIENT_TYPE = "FILLING"
SECOND_INGREDIENT_PRICE = 3.0

INGREDIENT_TEST_DATA = [
    ("SAUCE", "Сырный", 5.0),
    ("FILLING", "Котлета", 15.0),
    ("UNKNOWN", "Неизвестно", 0.0),
]
