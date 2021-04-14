def encrypt(input, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # LC = (LP+CH)MOD 26
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
            # criptografando
            index = (positionLetter+key) % len(alphabet)
            inputEncrypt += alphabet[index]
        else:
            inputEncrypt += ' '

    return inputEncrypt
def decrypt(input, key):
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

inputData = input('Insira o texto: ')
key = input('Insira a chave: ')
choice = input('Insira o número da ação que deseja que aconteça:\n1.Criptografar\n2.Descriptografar \n')

if int(choice) == 1: print(encrypt(inputData, int(key)))
elif int(choice) == 2: print(decrypt(inputData, int(key)))

