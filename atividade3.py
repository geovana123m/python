my_list = []

while True:
    options = input(
        '''
            Escolha uma opção:
            N: Novo Número;
            S: Soma
            Q: Sair
        '''
    ).lower()

    if options == 'n':
        numero = int(input("digite o numero"))
        my_list.append(numero)
    
    elif options == 's':
        print(sum(my_list))

    elif options == 'q':
        break

    def sum(list):
        result = 0
        for i in list:
            result = result + i
        return result