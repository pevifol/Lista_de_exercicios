''' Essa é uma simples demonstração de um menu. Ele poderia ser expandido para realmente realizar alguma função,  mas nesse caso não seria uma demonstração de meun, mas sim um menu funcional,
efetivamente quebrado o proposito inicial do mesmo.
Feito por Ruan felipe da silva e sousa, aluno de matemática aplicada'''
def menu():
    a=int(input('Escolha uma das opções: \n 1) Faça alguma coisa! \n 2) Faça outra coisa \n 3) Saia do programa. \n'))
    while a not in [1, 2, 3]:
        print('Você digitou um valor invalido. Por favor, digite 1, 2 ou 3.')
        a=input('Escolha uma das opções: \n 1) Faça alguma coisa! \n 2) Faça outra coisa \n 3) Saia do programa.')
    if a==1:
        print('Você selecionou 1)! Digite 2 para retornar ao menu inicial, ou qualquer outra coisa para encerrar.')
        b=int(input())
        if b == 2:
            menu()            
        else:
            print('Você encerrou o programa.')
            return
    if a==2:
        print('Você selecionou 2)! Digite 3 para retornar ao menu inicial, ou qualquer outra coisa para encerrar.')
        b=int(input())
        if b == 3:
            menu()            
        else:
            print('Você encerrou o programa.')
            return
    if a==3:
        print('Você selecionou encerrar o programa. Você não é muito divertido, sabia?')
        return
