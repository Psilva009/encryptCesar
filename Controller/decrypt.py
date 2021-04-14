class decrypt():
    def decrypt(self,input, key):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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