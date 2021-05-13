import unittest
from Controller.encrypt import encrypt
from Controller.alphabet import alphabet

class test_encrypt(unittest.TestCase):
    def test_verificar_retorno_word(self):
        # Arrange
        input = "teste"
        key = 10
        # Act
        response = encrypt().encrypt(input, key)

        # Assert
        self.assertEqual("cnbcn", response)
            
    def test_verificar_retorno_text(self):
        # Arrange
        input = "testando espaco"
        key = 10
        # Act
        response = encrypt().encrypt(input, key)

        # Assert
        self.assertEqual("cnbcjwmx nbyjlx", response)

    
if __name__ == '__main__':
    unittest.main()
