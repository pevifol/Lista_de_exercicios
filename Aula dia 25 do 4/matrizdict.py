'''Linhas e colunas'''
f=open("numlimcom.txt","r")#abre txt contendo arquivo de linhas e colunas
q=f.read().split(',')#separa numero de linhas e colunas
matrizdict={}#cria o dicionario
for z in range(int(q[0])):   #for loops para designar valores de índice das matrizes
    for i in range(int(q[1])):#    checa acima. ^
        x=str(z)+str(i) #calcula o valor do índice.
        matrizdict[x]=0.0#assigna valor para o dicionario, definindo o valor do elemento.
f.close()#fecha o arquivo. 
print('⌈{0},{1},{2}⌉\n⎸{3},{4},{5}⎹\n⌊{6},{7},{8}⌋'.format(matrizdict['00'],matrizdict['01'],matrizdict['02'],matrizdict['10'],matrizdict['11'],matrizdict['12'],matrizdict['20'],matrizdict['21'],matrizdict['22']))
#^ printa a matriz de forma ""bonita""
