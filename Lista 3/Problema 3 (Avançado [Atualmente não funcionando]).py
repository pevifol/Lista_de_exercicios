''' Problema 3 da Lista 3 de exercícios tópicos de mat aplicada A.'''
'''Originalmente, esse código foi criado para versão intermediaria do problema, mas descobri que'''
'''Ele poderia ser facilmente feito utilizando os.walk, já que tudo que eu precisava era de uma lista com o nome todos os arquivos TXT.'''
import os
def contpasta(a='.'):
    arquivos=os.listdir(a)
    listatxt=[]
    caminhos=[]
    caminhosabs=[]
    for root,dirs, files in os.walk(a):        
        if type(files)==type([]):#Todos os "files" que saem do os.walk são listas representando os diretorios, e agora vamos adicionar os arquivos dentro dos diretorios.
            for i in files:
                
                if i[-4:]=='.txt':#Verifica se os ultimos 4 digitos no path do arquivo são .txt.
                    listatxt.append(i)#adiciona a lista com o nome de todos os arquivos .txt                    
                else:
                    pass #Fechando o if.
        else: #Fechando o if.
            pass    
    for i in listatxt:
        caminhos.append(os.path.abspath(i))#encontrar o caminho absoluto pros arquivos TXT
    for i in caminhos:
        caminhosabs.append(i.replace('\\','/'))#troca o \\ nos path absolutos para \. Eu honestamente não sei pq ele coloca \\ em vez de \
    print(caminhosabs)    
    palavras=[] #Uma ferramenta para um truque no futuro :)
    palavrasfrequencia=[]#Outra ferramenta misteriosa.
    palavrasfrequenciadas=[]#Muitas ferramentas, meu amigo.  
    for i in caminhosabs: #Pega os arquivos TXT
        arquivo=open(i,'r')#Abre o arquivo.
        q=arquivo.read() #Lê os arquivos, formando uma grande string       
        z=q.split(" ")#Separa cada palavra criando uma lista
        for p in z:
            p.replace(',','')#remove ',' , '.' e ':' das palavras,            
            p.replace('.','')#Para evitar casos onde o programa confunda
            p.replace(':','')#a palavra seguido por pontuação da palavra sozinha.
        palavras+=z #Adiciona as palavras do texto criando uma megalista gigantesca contendo todas as palavras de todos os txt's,incluindo repetidas.
        arquivo.close()#Hora de fechar o que abrimos.
    for i in palavras:
        z=i.split('\n')#Remove palavras "juntadas" por quebra de linha.
        palavras.remove(i)#´<_` não parece funcionar pra algumas palavras, por motivos que desconheço.
        palavras+=z
    
    palavrasunicas=list(dict.fromkeys(palavras))#Remove palavras duplicadas da megalista, criando a lista de palavras unicas.    
    for x in palavrasunicas:#Hora de calcular a frequência das palavras.
        y=str(palavras.count(x))#Verifica a frequência de cada palavra no arquivo.
        palavrasfrequenciadas.append(x+' - '+y)#adiciona a palavra e sua frequencia separado por - a lista palavras.
    palavrasfrequenciadas.sort(key= lambda a: int(a.split(' - ')[1]) ,reverse=True)#Organizamos a lista baseado no valor de frequência da lista, do maior para o menor.  
    return palavrasfrequenciadas #termina a função.
            
            
            
            

            
        
        
        
        
