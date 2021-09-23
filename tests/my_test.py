import random
import string


class TestShortPhraseTest:
    def test_check_phrase(self):
        phrase = input("Set a phrase: ")
        symbols = "".join([random.choice(string.ascii_letters) for e in range(random.randrange(15, 16))])

        assert len(phrase) < len(symbols), f"Строка {phrase}, либо больше либо равна {symbols}"
