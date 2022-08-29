import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrenchNull(self):
        self.assertNotEqual(english_to_french(0),0)
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_frenchToEnglishNull(self):
        self.assertNotEqual(french_to_english(0),0)
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

if __name__ == "__main__":
    unittest.main()