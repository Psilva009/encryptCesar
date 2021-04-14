import unittest
from Controller.encrypt import encrypt

class test_encrypt(unittest.TestCase):
    def test_verificar_retorno(self):
        # Arrange
        input = "mariana"
        key = 5
        # Act
        response = encrypt().encrypt(input,key)
        
        # Assert
        self.assertEqual("rfwnfsf", response)

if __name__ == '__main__':
    unittest.main()