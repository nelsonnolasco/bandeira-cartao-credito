
import unittest
from card_detector import get_card_brand

class TestCardBrandDetection(unittest.TestCase):

    def test_visa(self):
        self.assertEqual(get_card_brand("4111111111111111"), "Visa")
        self.assertEqual(get_card_brand("4532 7153 3790 1241"), "Visa")

    def test_mastercard(self):
        self.assertEqual(get_card_brand("5105105105105100"), "MasterCard")
        self.assertEqual(get_card_brand("5399 9999 9999 9999"), "MasterCard")

    def test_amex(self):
        self.assertEqual(get_card_brand("378282246310005"), "American Express")
        self.assertEqual(get_card_brand("341111111111111"), "American Express")

    def test_invalid_input(self):
        self.assertEqual(get_card_brand("abc123"), "Número inválido")
        self.assertEqual(get_card_brand(""), "Número inválido")

    def test_unknown_brand(self):
        self.assertEqual(get_card_brand("9999999999999999"), "Bandeira desconhecida")

    def test_elo(self):
        self.assertEqual(get_card_brand("6362970000457013"), "Elo")
        self.assertEqual(get_card_brand("4389350000457013"), "Elo")

    def test_hipercard(self):
        self.assertEqual(get_card_brand("6062825624254001"), "Hipercard")

if __name__ == '__main__':
    unittest.main()
