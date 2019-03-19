'''
Ruan felipe da silva e sousa, aluno de matemática aplicada.
19/03/2019
DRE: 119041454.
A primeira função, vet(a), pergunta os valores dos vetores e retorna uma lista,
contendo seus valores. a segunda, pergunta os valores de 2 vetores
que deseja se somar, e soma as coordenadas e retorna o vetor resultado.
'''

def vet(a):
    d=[]
    z=0
    i=0
    while z < 10:       
        i+=1
        if i==1:
            x=input('Digite a valor da coordenada do vetor '+str(a)+' na '+str(i)+'° dimensão. Caso o vetor '+str(a)+' não se expanda mais em nenhuma dimensões além destas, digite k como resposta para interromper o loop: ')
            d.append(float(x))        
        if i!=1:
            x=input('Digite a valor da coordenada do vetor '+str(a)+' na '+str(i)+'° dimensão.')
            d.append(float(x)
        if x=='k':
                     break
                      
    return d    
def sumvet():
    a=vet(1)
    b=vet(2)
    teta=len(a)
    c=[]
    while len(a)<len(b):
        a.append(float(0))
    while len(b)<len(a):    
        b.append(float(0))
    for q in range(teta):
        alpha=a[q]
        beta=b[q]
        gamma=alpha+beta
        delta=float(gamma)
        c.append(delta)
    print('O vetor resultado vale:')
    print(c)    

            
