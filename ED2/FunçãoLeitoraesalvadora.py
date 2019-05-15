import os  #Uma biblioteca de código que nos permite trabalho com arquivos
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
    
        
        
        
        
    
    
    
    
