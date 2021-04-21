class decrypt():
    def decrypt(self,input, key, alphabet):
        inputDecrypt = ""
        for i in range(len(input)):
            letter = input[i]

            # verificando se é um espaço
            if letter != ' ':
                # verificando posição da letra do input
                for i in range(len(alphabet)):
                    if letter.lower() == alphabet[i]:
                        positionLetter = i
                        break
                # descriptografando
                index = (positionLetter - key) % len(alphabet)
                inputDecrypt += alphabet[index]
            else:
                inputDecrypt += ' '

        return inputDecrypt