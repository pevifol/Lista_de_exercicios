import os
'''Barriga é legal'''
def menu():
    '''Menu inicial da calculadora matricial'''
    q='''
          _______ _______        _______ _     _        _______ ______   _____   ______ _______      _______ _______ _______  ______ _____ _______ _____ _______                
 ___      |       |_____| |      |       |     | |      |_____| |     \ |     | |_____/ |_____|      |  |  | |_____|    |    |_____/   |   |         |   |_____| |           ___
          |_____  |     | |_____ |_____  |_____| |_____ |     | |_____/ |_____| |    \_ |     |      |  |  | |     |    |    |    \_ __|__ |_____  __|__ |     | |_____         
     Informe o que você deseja fazer: (Recomenda-se ao iniciar pela primeira vez ir na primeira opção para definir uma matriz, já que a lista começa vazia)
     1 - Manipular lista de matrizes
     2 - realizar operações com matrizes
     3 - alterar configurações do programa
     '''
    z = input(q)
    if z == '1':
        return manlist()
    if z == '2':
        return operações()
    if z == '3':
        return altconfig()

def manlist():
    '''Lista usada para manipular as matrizes'''
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
        print('1 - Criar uma nova matriz')
        print('2 - Ler backup (Acrescentar ou substituir)')
        print('3 - Inserir matriz identidade NxN')
        q=input('\nO que você deseja fazer? ')
        if q == '1':
              return criar_matriz()
        if q == '2':
              return ler_backup()
        if q == '3':
              return identidade()           
    print('Matrizes disponíveis para a visualização:')    
    for i in arquivos:
        c=str(arquivos.index(i)+1)+' - '+i
        print(c[:-4])
        z=arquivos.index(i)+1
    print('~ Outras opções ~')
    print(str(z+1)+' - Criar uma nova matriz')
    print(str(z+2)+' - Deletar matriz da lista')
    print(str(z+3)+' - Fazer backup da lista atual')
    print(str(z+4)+' - Zerar a lista de matriz')
    print(str(z+5)+' - Ler backup (Acrescentar ou substituir)')
    print(str(z+6)+' - Inserir matriz identidade NxN')
    c=input('\nO que você deseja fazer?: ')    
    if c==str(z+1):
        return criar_matriz()
    if c==str(z+2):
        print('Matrizes disponíveis para remoção:')    
        for i in arquivos:
            c=str(arquivos.index(i)+1)+' - '+i
            print(c[:-4])
        c=input('\nQual matriz você deseja remover?: ')   
        try:
            x=[arquivos[arquivos.index(c)]]
            return limpar_lista(x)
        except:
            print('\n Por favor, selecione um valor dentro da lista')
            return manlist()        
    if c==str(z+3):             
        return backup_matriz(arquivos)
    if c==str(z+4):
        return limpar_lista(arquivos)
    if c==str(z+5):
        return ler_backup()
    if c==str(z+6):
        return identidade()
    return alterar_matriz(arquivos[int(c)-1])     

def backup_matriz(a):    
    '''Recebe uma lista com os nomes de matrizes, e então faz backup dessas matrizes em uma pasta'''
    u=input('Digite o nome do backup que você deseja fazer:   ')
    xy=input('Você deseja deletar os arquivos originais? y/n: ')
    if not os.path.exists('./matrizes/backup/'+u):
        os.makedirs('./matrizes/backup/'+u)
    for i in a:
        x=open('./matrizes/'+i,'r')
        z=x.read()
        q=open('./matrizes/backup/'+u+'/'+i,'w')
        q.write(z)
        x.close()
        q.close()
    if xy == 'y':
        for i in a:
            os.remove('./matrizes/'+i)
        print('\nArquivos removidos com sucesso\n')        
    print('\n Backup realizado com sucesso!\n')        
    return menu()

def limpar_lista(a):
    ''' Recebe uma lista de matrizes, e remove elas da pasta de arquivos.'''
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
        print('A lista já está vazia.')
        return menu()    
    p=input('Você tem certeza que deseja fazer isso? y/n: ')    
    if p=='y':
        for i in a:
            os.remove('./matrizes/'+i)    
        print('\nArquivo removidos com sucesso com sucesso.\n')
        return menu()
    else:
        return manlist()
    
def ler_backup():
    '''Abre o backup feito na pasta'''
    arquivos = os.listdir("."+'/matrizes/backup')  
    if arquivos == []:
        print('Não parecem haver backups para serem lidos.')
        return manlist()
    print('Backups disponíveis para leitura: ')    
    for i in arquivos:
        c=str(arquivos.index(i)+1)+' - '+i
        print(c)
    c=input('Qual dos backups você deseja que seja lido?: ')
    p=input('Você deseja substituir em vez de adicionar a lista atual? y/n : ')
    if p == 'y':
        arquipos= os.listdir('./matrizes')
        limpar_lista(arquipos)
    try:
        arquivos = os.listdir('./matrizes/backup'+arquivos[c-1])
        for i in arquivos:
            x=open('./matrizes/backup/'+i,"r")            
            z=x.read().split('\n')
            p=open('./matrizes/'+i,'w')
            p.write(z)
            x.close()
            p.close()
        return manlist()
    except: #caso algo dê errado, a função vai executar esse bloco de código.
        print('Por favor, digite um numero.válido \n')
        return ler_backup()
    
def ver_matriz(a):
    '''Printa uma matriz recebida, perguntando se o ususario deseja alterar ela'''
    z=open('./matrizes/'+a,'r')
    x=z.read()
    print(x)
    x=x.split('\n')
    q=input('Você deseja fazer alguma alteração a essa matriz? y/n: ')
    if q == 'y':
        return alterar_matriz(x)
    else:
        return manlist()
    
def alterar_matriz(x):    
    '''Recebe uma matriz e altera ela'''
    p=input('Você deseja fazer uma alteração a qual linha?   ')
    if p>len(x):
        print('Por favor, selecione uma linha válida.')
        return alterar_matriz(x)
    y=input('Você deseja fazer uma alteração a qual elemento?  ')
    if y>len(x[1]):
        print('Por favor, selecione uma coluna válida ')
        return alterar_matriz(x)
    c=input('Defina o novo valor do elemento: ')
    x[p][y]=int(c)
    q=input('Você deseja realizar mais alguma alteração? y/n:  ')
    if q == 'y':
        return alterar_matriz(x)
    return manlist()

def salvarmatriz(a):
    b=input('Digite o nome da matriz que você deseja salvar: ')#Capta o nome da matriz
    if b == '':
        print('\nPor favor, dê um nome a sua matriz.\n')
        return salvarmatriz(a)
    x=open('./matrizes/'+b+'.txt','w')#Comando informando ao python que vamos criar/nomear um objeto
    try:
        for i in a:#a é uma lista, e portanto, vamos salvar cada "linha" dentro dela separadamente.
            x.write(i)#Escreve os elementos de a no arquivo.
        x.close()#Fecha o objeto que abrimos, encerrando a função
        return
    except:
        print('A matriz para ser salva está com algum problema. Por favor, tente novamente.\n')
        
def lermatriz():
    arquivos = os.listdir("."+'/matrizes')#lê todos os arquivos contidos onde o programa está.
    rmarquivos=[]
    for i in arquivos:
        if i[-4:] != '.txt' : 
            rmarquivos.append(i)#Salva o nome de todos os arquivos que NÃO são .txt
        else:
            pass
    for i in rmarquivos:
        arquivos.pop(arquivos.index(i))#Remove os arquivos que não são .txt

    if arquivos == []:
        print('Não parecem haver matrizes para serem lidas.')
        return
    print('Matrizes disponíveis para a leitura:')    
    for i in arquivos:
        c=str(arquivos.index(i)+1)+' - '+i
        print(c[:-4]) #Printa uma lista com todos os arquivos.
    c=input('Qual das matrizes você deseja que seja lida?: ')
    try:
        x=open('.'+str('/matrizes/'+arquivos[int(c)-1]),"r")
        z=x.read().split('\n')#lê a matriz de dentro da pasta.
        x.close()#fecha o que abrimos.
        return z #a matriz que desejamos está ai.
    except: #caso algo dê errado, a função vai executar esse bloco de código.
        print('Por favor, digite um numero.\n')
        return lermatriz()

#----------------------------------ESSE AQUI É O MENU ONDE O USUARIO ESCOLHE A OPERAÇÃO------------------------------------------------

def operações():
    print("+","-"*14,"Operações","-"*14,"+")  
    print("|                                         |")
    print("|  1 – Soma Matricial                     |")
    print("|  2 – Subtração Matricial                |")
    print("|  3 – Multiplicação Matricial            |")
    print("|  4 – Somar Linhas da Matriz             |")
    print("|  5 – Somar Colunas da Matriz            |")
    print("|  6 – Permutar Linhas                    |")
    print("|  7 – Permutar Colunas                   |")
    print("|  8 – Transposição de Matriz             |")
    print("|  9 – Multiplicação por Escalar          |")
    print("| 10 – Multiplicar Linha por Escalar      |")
    print("| 11 – Multiplicar Coluna por Escalar     |")
    print("| 12 – Inversão de matrizes quadradas 2x2 |")
    print("|                                         |")
    print("+","-"*39,"+")

    opção = int(input(print("Digite o numero da operação que você deseja realizar. ")))
    if opção < 1 or opção > 12: # serve para se a opção digitada não for valida
        print("Essa opção não é valida")
        a = input(print("Digite 1 para tentar escolher novamente ou digite 2 \n para voltar ao menu inicial. "))
        while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida
            print("Essa opção não é valida, tenta de novo ai")
            a= int(input(print("Digite 1 para tentar escolher novamente ou \ndigite 2 para voltar ao menu inicial. ")))
            
        if a == 1:
            return operações()
        else:
            return menu()
    else:# Aqui de acordo com a opção escolhida, o bagulho vai mandar pra uma função que
         # seleciona as matrizes da operação e depois vai devolver aqui pra operação rolar


        if opção == 1 or opção == 2:
            mz = escolher(opção)
            return soma_subt(mz[0],mz[1],opção)

        elif opção == 3:
            mz = escolher(opção)
            return multi_mat(mz[0],mz[1])

        elif opção == 4 or opção == 5:
            mz = escolher(opção)
            return som_lin_col(mz,opção)


        elif opção == 6 or opção == 7:
            mz = escolher(opção)
            return per_lin_col(mz,opção)


        elif opção == 8:
            mz = escolher(opção)
            return transpor(mz)

        elif opção == 9:
            mz = escolher(opção)
            return multi_esc(mz)

        elif opção == 10 or opção == 11:
            mz = escolher(opção)
            return multi_lin_col_esc(mz,opção)

        else:
            mz = escolher(opção)
            return inversão(mz)

#-----------------------ESSA FUNÇÃO FAZ O USUARIO ESCOLHER AS MATRIZES QUE SERÃO USADAS NA OPERAÇÃ0-------------------------------
#-----------PODE PARECER DESNECESSARIO, MAS EU FIZ PRA CONCENTRAR EM UM LUGAR SÓ, TODOS OS TRATAMENTOS DE EXCESSÃO----------------
def escolher(x):
    if x > 0 and x < 4:
        a = int(input(print("Digite 1 para escolher matriz 1 da memoria ou\n digite 2 para digitar matriz 1. ")))
        while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida
            print("Essa opção não é valida, tenta de novo ai")
            a= int(input(print("Digite 1 para escolher matriz 1 da memoria ou\n digite 2 para digitar matriz 1. ")))
        if a == 1:
            mat1 = lermatriz()
        else:
            mat1 = matriz_criar()

        a = int(input(print("Digite 1 para escolher matriz 2 da memoria ou\n digite 2 para digitar matriz 2. ")))
        while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida ( é o unico jeito que eu sei )
            print("Essa opção não é valida, tenta de novo ai")
            a = int(input(print("Digite 1 para escolher matriz 2 da memoria ou\n digite 2 para digitar matriz 2. ")))
        if a == 1:
            mat2 = lermatriz()
        else:
            mat2 = matriz_criar()

        if x == 1 or x == 2:
            if len(mat1)!=len(mat2) or len(mat1[0])!=len(mat2[0]):
                print('Impossível realizar operação, pois suas matrizes não possuem o mesmo número de linhas ou colunas.')
                a = input(print("Digite 1 para escolher outras matrizes ou digite 2 para retornar ao menu inicial. "))
                while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida ( é o unico jeito que eu sei )
                    print("Essa opção não é valida, tenta de novo ai")
                    a = int(input(print("Digite 1 para escolher outras matrizes ou digite 2 para retornar ao menu inicial. ")))
                if a == 1:
                    final = escolhe(x)
                else:
                    return menu()
            else:
                final = [mat1,mat2]

        else:
            if len(mat1[0])!=len(mat2):
                print('Impossível realizar operação,pois a matriz 1 não possui o\n numero de colunas igual ao numero de linhas da matriz 2.')
                a = input(print("Digite 1 para escolher outras matrizes ou digite 2 para retornar ao menu inicial. "))
                while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida ( é o unico jeito que eu sei )
                    print("Essa opção não é valida, tenta de novo ai")
                    a = int(input(print("Digite 1 para escolher outras matrizes ou digite 2 para retornar ao menu inicial. ")))
                if a == 1:
                    final = escolhe(x)
                else:
                    return menu()
            else:
                final = [mat1,mat2]
                
        return (final)

    elif x > 3 and x < 8:
        a = int(input(print("Digite 1 para escolher matriz da memoria ou\n digite 2 para digitar matriz. ")))
        while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida
            print("Essa opção não é valida, tenta de novo ai")
            a= int(input(print("Digite 1 para escolher matriz da memoria ou\n digite 2 para digitar matriz. ")))
        if a == 1:
            mat1 = lermatriz()
        else:
            mat1 = matriz_criar()

        if x == 4 or x == 6:
            if len(mat1) < 2:
                print('Impossível realizar operação, pois suas matriz não possui linhas suficientes. ')
                a = input(print("Digite 1 para escolher outra matriz ou digite 2 para retornar ao menu inicial. "))
                while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida ( é o unico jeito que eu sei )
                    print("Essa opção não é valida, tenta de novo ai")
                    a = int(input(print("Digite 1 para escolher outra matriz ou digite 2 para retornar ao menu inicial. ")))
                if a == 1:
                    final = escolhe(x)
                else:
                    return menu()
            else:
                final = mat1

        else:
            if len(mat1[0]) < 2:
                print('Impossível realizar operação, pois suas matriz não possui colunas suficientes. ')
                a = input(print("Digite 1 para escolher outra matriz ou digite 2 para retornar ao menu inicial. "))
                while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida ( é o unico jeito que eu sei )
                    print("Essa opção não é valida, tenta de novo ai")
                    a = int(input(print("Digite 1 para escolher outra matriz ou digite 2 para retornar ao menu inicial. ")))
                if a == 1:
                    final = escolhe(x)
                else:
                    return menu()
            else:
                final = mat1
                
        return (final)

    else:
        a = int(input(print("Digite 1 para escolher matriz da memoria ou\n digite 2 para digitar matriz. ")))
        while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida
            print("Essa opção não é valida, tenta de novo ai")
            a= int(input(print("Digite 1 para escolher matriz da memoria ou\n digite 2 para digitar matriz. ")))
        if a == 1:
            mat1 = lermatriz()
        else:
            mat1 = matriz_criar()

        return (final)
#-----------------------ESSA FUNÇÃO AQUI É SÓ PRO CARA DIGITAR A MATRIZ DA OPERAÇÃO, MAS É DIFERENTE DO CRIAR_MATRIZ------------------
#---------------------------PORQUE NÃO DEIXA O USUARIO SALVAR A MATRIZ CRIADA NA MEMORIA, É SÓ PRA USAR NA CONTA---------------------
def matriz_criar():
    m=int(input(print("Sua matriz possui quantas linhas? ")))
    n=int(input(print("Sua matriz possui quantas colunas? ")))
    mat=[]
    for i in range(m):
        linha=[]
        for j in range(n):
            a = float(input(print("Qual o elemento da {0}° linha, {1}° coluna? ".format(i,j))))
            lista.append(a)
        mat.append(linha)
    
    print("Sua matriz é")
    print()
    print("+-"," "*(7*len(mat[0])-2),"-+")
    for i in range (len(mat)):
        print("| ",end="")
        for j in range (len(mat[0])):
            print(" {0:^5} ".format(x[i][j]),end="")

        print(" |")
    print("+-"," "*(7*len(mat[0])-2),"-+")
    
    resp = input(print("Digite 1 se a matriz estiver certa ou \nDigite 2 para digitar novamente. "))
    while resp!=1 and resp!=2:# aqui é pra garantir que digite uma opção valida
        print("Essa opção não é valida, tenta de novo ai")
        resp = int(input(print("Digite 1 se a matriz estiver certa ou \nDigite 2 para digitar novamente. ")))
    if resp == 1 :
        print("Tudo bem")
        return mat
                
    else:
        print("Tudo bem")
        return matriz_criar()   
    
#-------ESSA AQUI EU CRIEI SÓ PRA PRINTAR O RESULTADO QUE SAI DE UMA OPERAÇÃO E PERGUNTAR SE O USUARIO QUER SALVAR O RESULTADO-------
def resultado(x):
    
    print("O resultado é\n")
    print()
    print("+-"," "*(7*len(x[0])-2),"-+")
    for i in range (len(x)):
        print("| ",end="")
        for j in range (len(x[0])):
            print(" {0:^5} ".format(x[i][j]),end="")

        print(" |")
    print("+-"," "*(7*len(x[0])-2),"-+")

    sal = input(print("Digite 1 para salvar o resultado \nDigite 2 para retornar ao menu de operações ou \nDigite 3 para retornar ao menu inicial. "))
        while sal!=1 and sal!=2 and sal!=3:# aqui é pra garantir que digite uma opção valida
            print("Essa opção não é valida, tenta de novo ai")
            sal = int(input(print("Digite 1 para salvar o resultado \nDigite 2 para retornar ao menu de operações ou \nDigite 3 para retornar ao menu inicial. ")))
    if sal == 1:
        salvarmatriz(x):
        return menu()
    
    elif sal == 2:
        return operações()
    else:
        return menu()
#-----------------------------AQUI SÃO TODAS AS OPERAÇÕES PRONTAS ( TIRANDO A INVERSÃO 2X2 )--------------------------------
def soma_subt(x,y,z):
    m = int(len(x))
    n = int(len(x[0]))
    mat = []
        for i in range (m):                          
            linha=[]
            for j in range (n):  
                if z == 1:
                    som = float(x[i][j]) + float(y[i][j])
                    linha.append(som)
                if z == 2:
                    som = float(x[i][j]) - float(y[i][j])
                    linha.append(som)
            mat.append(linha)
        
    return resultado(mat)             
#----------------------------------------------------------------------------------------------------------------
def multi_mat(x,y):
    m = int(len(x))
    n = int(len(y[0]))
    k = int(len(y))
    mat = []
    for i in range (m):
        linha=[]
        for j in range (n):
            elem = 0
            for l in range(k):
                elem += float(x[i][l])*float(y[l][j])
                linha.append(elem)
        mat.append(linha)    
    
    return resultado(mat)
#---------------------------------------------------------------------------------------------------------------
def som_lin_col(x,y):
    m = int(len(x))
    n = m
    per = []
    if y == 4:
        pa = 'linha'
    else:
        pa = 'coluna'
            
    l1 = int(input(print('Digite o numero da {} que em que o resultado permanecera. '.format(pa))))
    l2 = int(input(print('Digite o numero da {} que você somara a linha escolhida a cima. '.format(pa))))
    for i in range(n):
        linha=[]
        if i == (l1-1):
            for j in range (n):
                if j == (l1-1) or j == (l2-1):
                    p = 1
                else:
                    p = 0
                linha.append(p)
           
        else:
            for j in range (n):
                if j == i:
                    p = 1
                else:
                    p = 0
                linha.append(p)
        per.append(linha)
           
    if y == 4:
        return multi_mat(per,x)
    else:
        return multi_mat(x,per)
#--------------------------------------------------------------------------------------------------------------------
def per_lin_col(x,y):
    per = []
    if y == 6:
        pa = 'linha'
        m = int(len(x))
        n = m
    else:
        pa = 'coluna'
        m = int(len(x[0]))
        n = m
        
    l1 = int(input(print('Digite o numero de uma das {}s que você quer permutar. '.format(pa))))
    l2 = int(input(print('Digite o numero da outra {} que você quer permutar. '.format(pa))))
    for i in range(n):
        linha=[]
        if i == (l1-1):
            for j in range (n):
                if j == (l2-1):
                    p = 1
                else:
                    p = 0
                linha.append(p)
         
        elif i == (l2-1):
            for j in range (n):
                if j == (l1-1):
                    p = 1
                else:
                    p = 0
                linha.append(p)
        else:
            for j in range (n):
                if j == i:
                    p = 1
                else:
                    p = 0
                linha.append(p)
        per.append(linha)
           
    if y == 6:
        return multi_mat(per,x)
    else:
        return multi_mat(x,per) 
#----------------------------------------------------------------------------------------------------------------
def transpor(x):
    m = int(len(x[0]))
    n = int(len(x))                   
    mat = []
    
    for i in range (m):                          
        linha=[]
        for j in range (n):
            troc = x[j][i]
            linha.append(troc)
        mat.append(troc)
        
   return resultado(mat)
#---------------------------------------------------------------------------------------------------------------
def multi_esc(x):
    k=int(input('Digite o valor pelo qual deseja que a matriz seja multiplicada. '))
    m = int(len(x))
    n = int(len(x[0]))                   
    mat = []
    
    for i in range (m):                          
        linha=[]
        for j in range (n):
            multi = x[i][j]*k
            linha.append(multi)
        mat.append(linha)
        
   return resultado(mat)
#----------------------------------------------------------------------------------------------------------------
def multi_lin_col_esc(x,y):
    mat = []
    if y == 10:
        pa = 'linha'
        m = int(len(x))
        n = m
    else:
        pa = 'coluna'
        m = int(len(x[0]))
        n = m
    k=int(input('Digite o valor pelo qual deseja que a {} da matriz seja multiplicada. '.format(pa)))
    l1 = int(input(print('Digite o numero da {0} que você quer multiplicar por {1}. '.format(pa,k))))
    for i in range(n):
        linha=[]
        if i == (l1-1):
            for j in range (n):
                if i == j:
                    p = k
                else:
                    p = 0
        else: 
            for j in range (n):
                if j == i:
                    p = 1
                else:
                    p = 0
            linha.append(p)   
        mat.append(linha)
    
    if y == 6:
        return multi_lin_col_esc(mat,x)
    else:
        return multi_lin_col_esc(x,mat) 
#-----------------------------------------------------------------------------------------------------------------
def inversão(x):
