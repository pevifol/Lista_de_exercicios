'''
Este programa calcula o resultado da exponênciação de 2 numeros inteiros,
e em seguida calcula a soma de seus algarismos na base 10.
A função calcalg(x,y) recebe como parametros o valor base (x) e o expoente (y)
já a função sumalg(x), recebe como parametro o numero que se deseja saber a soma
de seus algarismos.
Aluno: Ruan felipe da silva e sousa
DRE:119041454
'''
def sumalg(x):
    q=tuple(str(x))
    z=0
    x=len(q)
    for p in range(x):        
        z+=int(q[p])
    return z    
def calcalg(x,y):
    q=x**y    
    return sumalg(q)
print('Como desejamos saber a soma dos dígitos de um 2^1001, vamos ordenar que o computador faça calcalg(2,1001):')
calcalg(2,1001)
