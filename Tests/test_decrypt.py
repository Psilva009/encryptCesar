import unittest
from Controller.decrypt import decrypt
from Controller.alphabet import alphabet

class test_decrypt(unittest.TestCase):
    def test_verificar_retorno(self):
        # Arrange
        input = ["rfwnfsf", "фхнжйч"]
        key = 5
        choiceAlphabet = ['1','2']
        # Act
        expect=['mariana','привет']
        for i in range(len(input)):
            a = alphabet.getAlphabet(choiceAlphabet[i])
            response = decrypt().decrypt(input[i],key,a)
        
            # Assert
            self.assertEqual(expect[i], response)

if __name__ == '__main__':
    unittest.main()