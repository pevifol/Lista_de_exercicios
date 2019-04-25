'''Linhas e colunas'''
z=open("numlimcom.txt","r")#abre txt contendo arquivo de linhas e colunas
q=z.read().split(',')
matriz=[0.0]*int(q[0])
for i in range(len(matriz)):
    matriz[i]=[0.0]*int(q[1])
for i in matriz:
    print(i)
