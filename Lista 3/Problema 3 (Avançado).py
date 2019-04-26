''' Problema 3 da Lista 3 de exercícios tópicos de mat aplicada A.'''
'''Originalmente, esse código foi criado para versão intermediaria do problema, mas descobri que'''
'''Ele poderia ser facilmente feito utilizando os.walk, já que tudo que eu precisava era de uma lista com o nome todos os arquivos TXT.'''
import os
def contpasta(a='.'):       
    caminhos=[] #Ferramenta onde salvaremos os caminhos relativos para os arquivos.
    for root,dirs, files in os.walk(a):#Caminho pelo diretorio e os subdiretorios procurando os arquivos.
        for i in files:#for loop pegando o nome individual de cada arquivo para encontrar caminho relativo.
            if i[-4:]=='.txt':#Verifica se os ultimos 4 digitos no path do arquivo são .txt.
                caminhos.append(root+'\\'+i)#adiciona a lista com o caminho relativo pro arquivo.
            else:
                pass#Fechando if.
    palavras=[] #lista para gravar todas as palavras nos TXT's.
    palavrasfrequenciadas=[]#Lista final, frequenciada.
    for i in caminhos: #Pega os arquivos TXT.
        arquivo=open(i,'r')#Abre o arquivo.
        q=arquivo.read() #Lê os arquivos, formando uma grande string.       
        z=q.split(" ")#Separa cada palavra criando uma lista.
        for p in z:
            p.replace(',','')#remove ',' , '.' e ':' das palavras,            
            p.replace('.','')#Para evitar casos onde o programa confunda
            p.replace(':','')#a palavra seguido por pontuação da palavra sozinha.
        palavras+=z #Adiciona as palavras do texto criando uma megalista gigantesca contendo todas as palavras de todos os txt's,incluindo repetidas.
        arquivo.close()#Hora de fechar o que abrimos.
    for i in palavras:        
        z=i.split('\n')#separa palavras "juntadas" por quebra de linha.
        palavras.remove(i)#Remove a palavra juntada que quebramos no exercicio anterior da lista original.
        palavras+=z#re-adiciona as palavras separadas para a lista original.
    for i in palavras:
        z=i.lower()#transforma todas as palavras pra letra minuscula.
        palavras.remove(i)#remove palavra "grande"
        palavras+=z#re-adiciona as palavras removidas anteriormente.
    palavrasunicas=list(dict.fromkeys(palavras))#Remove palavras duplicadas da megalista, criando a lista de palavras unicas.    
    for x in palavrasunicas:#Hora de calcular a frequência das palavras.
        y=str(palavras.count(x))#Verifica a frequência de cada palavra no arquivo.
        palavrasfrequenciadas.append(x+' - '+y)#adiciona a palavra e sua frequencia separado por - a lista palavras.
    palavrasfrequenciadas.sort(key= lambda a: int(a.split(' - ')[1]) ,reverse=True)#Organizamos a lista baseado no valor de frequência da lista, do maior para o menor.
    print('A lista das palavras frequênciadas é a seguinte:')#Comentário para ficar bonito
    return palavrasfrequenciadas #Termina a função.

            
            

            
        
        
        
        
