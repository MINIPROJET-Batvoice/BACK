import re

class TextValidator:
    def __init__(self, character_set):
        self.character_set = character_set

    def validate(self, text, error_messages):
        is_valid = True
        if not self.validate_character_set(text):
            is_valid = False
            error_messages.append('The transcription text contains invalid characters.')
        if not self.validate_capital_letters(text):
            is_valid = False
            error_messages.append('The transcription text contains errors related to the use of capital letters.')
        if not self.validate_spaces(text):
            is_valid = False
            error_messages.append('The transcription text contains multiple consecutive spaces.')
        if not self.validate_end_characters(text):
            is_valid = False
            error_messages.append('The transcription text contains punctuation or separation errors.')
        return is_valid

    def validate_character_set(self, text):
        for char in text:
            if char not in self.character_set:
                return False
        return True

    def validate_capital_letters(self, text):
        words = re.findall(r'\b\w+\b', text)
        for word in words:
            if word.isupper() and len(word) > 1:
                continue
            elif not word[0].isupper():
                return False
            elif word[0].islower() and any(letter.isupper() for letter in word[1:]):
                return False
        return True

    def validate_spaces(self, text):
        if re.search(r'\s{2,}', text):
            return False
        return True

    def validate_end_characters(self, text):
        if re.search(r'[?!.]\s*[a-z]|[,;:]\s*[a-z]', text):
            return False
        return True
