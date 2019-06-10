import os
lnomes=[]
if not os.path.exists('./alunos'):
        os.makedirs('./alunos')
arquivos = os.listdir("."+'/alunos')
rmarquivos=[]
class laluno:
    def __init__(self, nome='joão', p1=0, p2=0, pf=0, p2a=None, DRE=None, freq=0, curso=None, período=None):
        self.notas=[p1,p2,pf,p2a]
        lnomes.append(nome),lnomes.append(DRE)
        self.freq=freq
        self.curso=curso
        self.período=período
        with open('./alunos/'+nome+'.txt','w+') as s:
            s.write(str(self.notas)+'\n'+str(nome)+'\n'+str(DRE)+str(freq)+'\n'+str(curso)+'\n'+str(período))
def extralu(i):
    with open('./alunos/'+lnomes[i]) as s:
        q=s.read()
        a=q.split('\n')[1]#nome
        b=q.split('\n')[2]#DRE
        c=q.split('\n')[4]#curso
        d=q.split('\n')[5]#periodo
        e=q.split('\n')[0]#notas
        f=q.split('\n')[3]  #frequencia
    return a,b,c,d,e,f
        

def menu():
    for i in arquivos:
        if i[-4:] != '.txt' :
            rmarquivos.append(i)
        else:
            pass
    for i in rmarquivos:
        arquivos.pop(arquivos.index(i))
    f=input('''
Bem vindo a lista de Alunos de uma turma.
O que você deseja fazer?
1) Inserir um novo aluno
2) Consultar/Buscar informações de um aluno
3) Alterar informação de um aluno
4) Remover um aluno da lista
5) Salvar lista de arquivos''')
    if f == '1':
        a=input('Digite o nome do aluno: ')
        b=input('Digite o DRE do aluno: ')
        c=input('Digite o curso do aluno: ')
        d=input('Digite o período do aluno: ')
        try:
            aluno=laluno(a,0,0,0,0,b,0,c,d)
        except:
            print('Ocorreu um erro durante o registro do aluno. Retornando ao menu inicial...')
        finally:
            menu()
    if f == '2':
        f=input('Digite 1 para procurar na lista de alunos usando o DRE, ou 2 para procurar na lista de alunos usando o nome: ')
        if f==1:
            q=input('Digite o DRE ou parte do DRE do aluno:')
            aluno=[]
            for i in lnomes:
                if q in i:
                    aluno.append(index(i)-1)
        if f==2:
            q=input('Digite o nome ou parte do nome do aluno:')
            aluno=[]
            for i in lnomes:
                if q in i:
                    aluno.append(index(i)-1)
                pass    
        print('| Nome | DRE | Curso | Notas (p1,p2,pf e segunda chamada) | Período | Frequência |')
        print(aluno)
        for i in aluno:
            q='| {a} | {b} | {c} | {e} | {d} | {f} |'.format(extralu(i))
            print(q)
        print("-"*len(q))
        
            
            
            
