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
            
    def test_alfabeto_diferente_da_mensagem(self):
        # Arrange
        input = ['mariana','привет']
        key = 5
        choiceAlphabet = ['2','1']
        # Act
        expect = "Verifique se a mensagem usa letras do alfabeto que você escolheu..."

        for i in range(len(input)):
            a = alphabet.getAlphabet(choiceAlphabet[i])
            response = encrypt().encrypt(input[i],key,a)
        
            # Assert
            self.assertEqual(expect, response)
    
if __name__ == '__main__':
    unittest.main()