from Controller.encrypt import encrypt
from Controller.decrypt import decrypt

class main():

    print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

    inputData = input('Insira o texto: ')
    key = input('Insira a chave: ')
    choice = input('Insira o número da ação que deseja que aconteça:\n1.Criptografar\n2.Descriptografar \n')


    if int(choice) == 1: 
        res = encrypt().encrypt(inputData,int(key))
        print(res)

    elif int(choice) == 2: 
        res = decrypt().decrypt(inputData, int(key))
        print(res)

