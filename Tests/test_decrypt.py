import unittest
from Controller.decrypt import decrypt

class test_decrypt(unittest.TestCase):
    def test_verificar_retorno_word(self):
        # Arrange
        input = "cnbcn"
        key = 10
        # Act
        response = decrypt().decrypt(input,key)
        
        # Assert
        self.assertEqual("teste", response)

    def test_verificar_retorno_text(self):
        # Arrange
        input = "cnbcjwmx nbyjlx"
        key = 10
        # Act
        response = decrypt().decrypt(input,key)
        
        # Assert
        self.assertEqual("testando espaco", response)    



if __name__ == '__main__':
    unittest.main()
