import csv
d={}
q=[0,0,0,0,0,0,0,0,0]
with open("perfil_eleitorado_ATUAL.txt", newline='',encoding='Latin 1') as arqcsv:
    dados = csv.reader(arqcsv, delimiter=";")
    for lin in dados:
        d[lin[7]]=lin[7]
        c=list(d)
        q[c.index(lin[7])]+=int(lin[8])
x=0
print('-----------------------------------------------------------------------------------')
for i in range(9):
    print(' Escolaridade: '+c[i]+' -- Quantidade: '+str(q[i]))
    x+=q[i]
print(' Total: '+str(x))    
print('-----------------------------------------------------------------------------------')
'''Nome dos alunos | DRE'''
'''Ruan Felipe da silva e sousa | 119041454'''
'''Felipe chen wu | 119055063'''
'''Igor torres | 119034669 '''
'''Grupo 2 -- Distribuição por escolaridade.'''
