import unittest
from .validator import TextValidator


class TestTextValidator(unittest.TestCase):
    def setUp(self):
        character_set = "()'aAàÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ "
        self.validator = TextValidator(character_set)

    def test_character_set(self):
        self.assertTrue(self.validator.validate_character_set("Hello World"))

    def test_capital_letters(self):
        self.assertTrue(self.validator.validate_capital_letters("Hello world"))

    def test_spaces(self):
        self.assertTrue(self.validator.validate_spaces("Hello World"))
        self.assertFalse(self.validator.validate_spaces("Hello  World"))

    def test_end_characters(self):
        self.assertTrue(self.validator.validate_end_characters("Hello World. How are you?"))
        self.assertTrue(self.validator.validate_end_characters("Hello World, How are you?"))

    def test_all_tests(self):
        self.assertTrue(self.validator.validate_character_set("Hello World"))
        self.assertTrue(self.validator.validate_capital_letters("Hello World"))
        self.assertTrue(self.validator.validate_spaces("Hello World"))
        self.assertTrue(self.validator.validate_end_characters("Hello World. How are you?"))


if __name__ == '__main__':
    unittest.main()
