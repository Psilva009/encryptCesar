class encrypt():
    def encrypt(self, input, key, alphabet):
        inputEncrypt = ""
        for i in range(len(input)):
            letter = input[i]

            # verificando se é um espaço
            if letter != ' ':
                # verificando posição da letra do input
                for i in range(len(alphabet)):
                    if letter.lower() == alphabet[i]:
                        positionLetter = i
                        break
                    else:
                        return "Verifique se a mensagem usa letras do alfabeto que você escolheu..."
                # criptografando
                index = (positionLetter+key) % len(alphabet)
                inputEncrypt += alphabet[index]
            else:
                inputEncrypt += ' '

        return inputEncrypt