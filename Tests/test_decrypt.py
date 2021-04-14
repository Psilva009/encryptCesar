import unittest
from Controller.decrypt import decrypt

class test_decrypt(unittest.TestCase):
    def test_verificar_retorno(self):
        # Arrange
        input = "rfwnfsf"
        key = 5
        # Act
        response = decrypt().decrypt(input,key)
        
        # Assert
        self.assertEqual("mariana", response)

if __name__ == '__main__':
    unittest.main()