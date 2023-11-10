import unittest
from .validator import TextValidator


class TestTextValidator(unittest.TestCase):
    def setUp(self):
        character_set = "()'aAàÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ "
        self.validator = TextValidator(character_set)

    def test_character_set(self):
        self.assertTrue(self.validator.validate_character_set("Audio transcription "))

    def test_capital_letters(self):
        self.assertTrue(self.validator.validate_capital_letters("Audio Transcription"))

    def test_spaces(self):
        self.assertTrue(self.validator.validate_spaces("audio transcription"))

    def test_end_characters(self):
        self.assertTrue(self.validator.validate_end_characters("audio transcription ?"))




if __name__ == '__main__':
    unittest.main()
