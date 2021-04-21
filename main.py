from Controller.encrypt import encrypt
from Controller.decrypt import decrypt
from Controller.alphabet import alphabet

class main():

    continuar = '1'
    while(continuar == '1'):
        inputData = input('Insira o texto: ')
        key = input('Insira a chave: ')
        num = input('Insira o número do alfabeto que deseja :\n1.Português/Inglês\n2.Russo\n')
        a = alphabet.getAlphabet(num)
        choice = input('Insira o número da ação que deseja que aconteça:\n1.Criptografar\n2.Descriptografar \n')
    

        if int(choice) == 1: 
            res = encrypt().encrypt(inputData,int(key), a)
            print(res)

        elif int(choice) == 2: 
            res = decrypt().decrypt(inputData, int(key), a)
            print(res)

        continuar = input('Insira 0 para encerrar ou 1 para continuar...\n')
        
