''' Problema 3 da Lista 3 de exercícios tópicos de mat aplicada A.'''
import os
def contpasta(a='.'):
    arquivos=os.listdir(a)
    listatxt=[]
    for txt in arquivos:
        if txt[-4:]=='.txt':#Verifica se os ultimos 4 digitos no path do arquivo são .txt.
            listatxt.append(txt)#Cria uma lista com o nome de todos os arquivos .txt
        else:                   #no diretorio.
            pass
    palavras=[] #Uma ferramenta para um truque no futuro :)
    palavrasfrequencia=[]#Outra ferramenta misteriosa.
    palavrasfrequenciadas=[]#Muitas ferramentas, meu amigo.
    print(listatxt)
    for i in listatxt: #Pega os arquivos TXT
        arquivo=open(i,'r')
        q=arquivo.read() #Lê os arquivos, formando uma grande string       
        z=q.split(" ")#Separa cada palavra criando uma lista
        for p in z:
            p.replace(',','')#remove ',' , '.' e ':' das palavras,            
            p.replace('.','')#Para evitar casos onde o programa confunda
            p.replace(':','')#a palavra seguido por pontuação da palavra sozinha.
        palavras+=z #Adiciona as palavras do texto criando uma megalista gigantesca contendo todas as palavras de todos os txt's,incluindo repetidas.
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
            
            
            
            

            
        
        
        
        
