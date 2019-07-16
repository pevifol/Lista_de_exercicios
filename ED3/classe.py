import os
'''ED3 - Calculadora matricial baseada em classe'''
'''Classe central - Matriz'''
class matriz():
    def  __init__(self,nome=None):
        if not os.path.exists('./matrizes'):
            os.makedirs('./matrizes')
        if not os.path.exists('./matrizes/backup'):
            os.makedirs('./matrizes/backup')
#O código acima verifica se existem as pastas necessarias para backup e salvamento de arquivo,
#e cria caso elas não existam
        if nome == None:
            self.nome=input('Digite o nome do arquivo da matriz: ')
            try:
                self.Nlinhas=int(input('Digite o numero de linhas da matriz: '))
                self.Ncolunas=int(input('Digite o numero de colunas da matriz: '))
            except:
                print("Por favor digite um valor válido para o numero de linhas/colunas. Utilizando valor padrão de 1x1")
                self.Nlinhas=1
                self.Ncolunas=1            
            self.diagonal=False
#Cria espaço para armazenar numero de linhas e colunas para verificações futuras.
            try:
                with open('./matrizes/'+self.nome,'w') as matriz:
                    for i in range(self.Nlinhas):
                        lista=''
                        for p in range(self.Ncolunas):
                            lista+=input('Digite o '+ str(p+1)+'° elemento da '+str(i+1)+'° linha: ')+','
                        try:
                            matriz.write(lista+'\n')
                        except:
                            print("Erro desconhecido ocorrido durante tentativa de gravar valor no arquivo, descontinuando operação.")
#Cria arquivo que contem as matrizes. Cada linha do arquivo é uma linha da matriz.
            if self.diagon() == True:
                self.diagonal=True
                a=self.v()
                os.remove("./matrizes/"+self.nome)
                with open('./matrizes/'+self.nome,'w') as matriz:
                    matriz.write('d'+','+str(self.Nlinhas)+','+str(self.Ncolunas)+'\n')
                    for i in range(min(self.Nlinhas,self.Ncolunas)):
                        matriz.write(a[i][i]+'\n')
            else:
                if self.diagonf() == True:
                    self.diagonalinf=True
                    a=self.v()
                    os.remove("./matrizes/"+self.nome)
                    with open('./matrizes/'+self.nome,'w') as matriz:
                        matriz.write("df"+','+str(self.Nlinhas)+','+str(self.Ncolunas)+'\n')
                        for i in range(self.Nlinhas):
                            lista=''
                            for j in range(self.Ncolunas):
                                if i<=j:
                                    lista+=a[i][j]
                            matriz.write(lista+'\n')                        
                if self.diagons() == True:
                    self.diagonalsup=True
                    a=self.v()
                    os.remove("./matrizes/"+self.nome)
                    with open('./matrizes/'+self.nome,'w') as matriz:
                        matriz.write('ds'+','+str(self.Nlinhas)+','+str(self.Ncolunas)+'\n')
                        for i in range(self.Nlinhas):
                            lista=''
                            for j in range(self.Ncolunas):
                                if i>=j:
                                    lista+=a[i][j]
                            matriz.write(lista+'\n')
          #Salvando memória.
        else:
            self.nome=nome
            with open('./matrizes/'+self.nome,'r') as matriz:
                z=matriz.read().split('\n')
                x=map(lambda x: x.split(','),z)
                a=x[0][0]
                if a == "d" or a == "df" or a == "ds" :
                    self.Nlinhas=x[0][1]
                    self.Ncolunas=x[0][2]
                else:
                    self.Nlinhas=len(x)
                    self.Ncolunas=len(x[0])            
    def v(self):
        with open('./matrizes/'+self.nome,'r') as matriz:
            z=matriz.read().split('\n')
            x=map(lambda x: x.split(','),z)
        if x[0][0] == "d" or x[0][0] == "df" or x[0][0] == "ds" :
            return "Função errada, parceiro. Utilize a função vd."
        return x
    def diagons(self):
        with open('./matrizes/'+self.nome,'r') as matriz:
            x=matriz.read().split('\n')
            x=map(lambda x: x.split(','),x)
            for i in range(self.Ncolunas):
                for j in range (self.Nlinhas):
                    if j > i:
                        if x[j][i] != '0':
                            return False
            return True
    def diagonf(self):
        with open('./matrizes/'+self.nome,'r') as matriz:
            x=matriz.read().split('\n')
            x=map(lambda x: x.split(','),x)
            for i in range(self.Ncolunas):
                for j in range (self.Nlinhas):
                    if j < i:
                        if x[j][i] != '0':
                            return False
            return True
    def diagon(self):
        if self.diagonf() == True and self.diagons() == True:
            return True
        return False
        
 #verifica se a matriz é diagonal superior/inferior ou diagon
    def __add__(self,x):
        if self.Nlinhas != x.Nlinhas or self.Ncolunas != x.Ncolunas:
            return "Não é possível somar essas matrizes. Numero de linhas/colunas é diferente"
        a=self.v()
        b=x.v()
        c=[]
        for i in range(self.Nlinhas):
            q=[]
            for j in range(self.Ncolunas):
                c=a[i][j]+b[i][j]
                q.append(c)
            c.append(q)
        return c
    def __sub__(self,x):
         if self.Nlinhas != x.Nlinhas or self.Ncolunas != x.Ncolunas:
            return "Não é possível subtrair essas matrizes. Numero de linhas/colunas é diferente"
        a=self.v()
        b=x.v()
        c=[]
        for i in range(self.Nlinhas):
            q=[]
            for j in range(self.Ncolunas):
                c=a[i][j]-b[i][j]
                q.append(c)
            c.append(q)
        return c
    def __mul__(self,x):
        if type(x) == int:
            a=self.v()
            for i in range(self.Nlinhas):
                for j in range(self.Ncolunas):
                    a[i][j]=a[i][j]*k
            return a
        if self.Ncolunas != x.Nlinhas:
            return "Não é possível multiplicar essas matrizes! Numero de colunas da primeira é diferente do numero de linhas da segunda."
        q = [[0 for row in range(x.Ncolunas)] for col in range(self.Nlinhas)]
        a=self.v()
        b=x.v()
        for i in range(self.Nlinhas):
            for j in range(x.Ncolunas):
                for k in range(x.Nlinhas):
                    q[i][j] += a[i][k]*b[k][j]
        return q
 #magic methods ftw
                            
            
