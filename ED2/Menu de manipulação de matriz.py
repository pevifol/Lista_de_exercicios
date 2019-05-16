import os
def menu():
    q='''
          _______ _______        _______ _     _        _______ ______   _____   ______ _______      _______ _______ _______  ______ _____ _______ _____ _______                
 ___      |       |_____| |      |       |     | |      |_____| |     \ |     | |_____/ |_____|      |  |  | |_____|    |    |_____/   |   |         |   |_____| |           ___
          |_____  |     | |_____ |_____  |_____| |_____ |     | |_____/ |_____| |    \_ |     |      |  |  | |     |    |    |    \_ __|__ |_____  __|__ |     | |_____         
     Informe o que você deseja fazer: (Recomenda-se ao iniciar pela primeira vez ir na primeira opção para definir uma matriz, já que a lista começa vazia)
     1 - Manipular lista de matrizes
     2 - realizar operações com matrizes
     3 - alterar configurações do programa                                                                                                                                                                            '''
    z = input(q)
    if z == 1:
        return manlist()
    if z == 2:
        return opmatriz()
    if z == 3:
        return altconfig()
def manlist():    
    z=0
    if not os.path.exists('./matrizes'):
        os.makedirs('./matrizes')
    if not os.path.exists('./matrizes/backup'):
        os.makedirs('./matrizes/backup')    
    arquivos = os.listdir("."+'/matrizes')
    rmarquivos=[]
    for i in arquivos:
        if i[-4:] != '.txt' : 
            rmarquivos.append(i)
        else:
            pass
    for i in rmarquivos:
        arquivos.pop(arquivos.index(i))
    if arquivos == []:
        z=input('Não parecem haver matrizes para serem lidas. Você deseja criar uma? y/n')
        if z == 'y':
            return criar_matriz()
        if z == 'n':
            print('\n Retornando ao menu inicial.\n')
            return menu()        
    print('Matrizes disponíveis para a leitura:')    
    for i in arquivos:
        c=str(arquivos.index(i)+1)+' - '+i
        print(c[:-4])
        z=i
    print(str(arquivos.index(z)+1)+' - Criar uma nova matriz')
    print(str(arquivos.index(z)+2)+' - Deletar matriz da lista')
    print(str(arquivos.index(z)+3)+' - Fazer backup da lista atual')
    print(str(arquivos.index(z)+4)+' - Zerar a lista de matriz')
    print(str(arquivos.index(z)+5)+' - Ler backup (Acrescentar ou substituir)')
    c=input('\nQual das matrizes você deseja que seja lida?: ')
    if c==str(arquivos.index(z)+1):
        return criar_matriz()
    if c==str(arquivos.index(z)+2):
        return remover_matriz()
    if c==str(arquivos.index(z)+3):
        u=input('Digite o nome do backup que você deseja fazer:   ')
        xy=input('Você deseja deletar os arquivos originais? y/n')
        if not os.path.exists('./matrizes/backup/'+u):
            os.makedirs('./matrizes/backup/'+u)
        for i in arquivos:
            x=open('./matrizes/'+i,'r')
            z=x.read()
            q=open('./matrizes/backup/'+u+'/'+i,'w')
            q.write(z)
            x.close()
            q.close()
        if xy == 'y':
            for i in arquivos:
                os.remove('./matrizes/'+i)
            print('Remoção removida com sucesso, meu parceiro')        
        print('\n Backup realizado com sucesso!\n')        
        return menu()
    if c==str(arquivos.index(z)+4):
        for i in arquivos:
                os.remove('./matrizes/'+i)
        print('\nArquivos pirocados até o oblivion com sucesso.\n')        
        return menu()        
    
    try:
        x=open('.'+str('/matrizes/'+arquivos[int(c)-1]),"r")
        z=x.read().split('\n')#lê a matriz de dentro da pasta.
        x.close()#fecha o que abrimos.
        return z #a matriz que desejamos está ai.
    except: #caso algo dê errado, a função vai executar esse bloco de código.
        print('Por favor, digite um numero.\n')
        return lermatriz()
        
