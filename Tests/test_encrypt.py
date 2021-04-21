import unittest
from Controller.encrypt import encrypt
from Controller.alphabet import alphabet

class test_encrypt(unittest.TestCase):
    def test_verificar_retorno(self):
        # Arrange
        input = ['mariana','привет']
        key = 5
        choiceAlphabet = ['1','2']
        # Act
        expect=["rfwnfsf", "фхнжйч"]

        for i in range(len(input)):
            a = alphabet.getAlphabet(choiceAlphabet[i])
            response = encrypt().encrypt(input[i],key,a)
        
            # Assert
            self.assertEqual(expect[i], response)


if __name__ == '__main__':
    unittest.main()