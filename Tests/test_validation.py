import unittest
from Controller.validation import validation

class test_validation(unittest.TestCase):
    def test_key_invalid(self):
        # Arrange
        input = "cnbcn"
        key = 30
        # Act
        response = validation().keyIsValid(int(key))

        # Assert
        self.assertEqual("A chave deve estar no intervalo da quantidade de letras do alfabeto.", response)

    def test_key_valid(self):
        # Arrange
        input = "cnbcn"
        key = 26
        # Act
        response = validation().keyIsValid(int(key))

        # Assert
        self.assertEqual("", response)

    if __name__ = '__main__':
        unittest.main()
