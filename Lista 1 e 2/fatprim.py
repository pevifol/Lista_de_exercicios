'''
programa para fatorar numeros.
Não parece funcionar para numeros muito grandes. Eu faço 0 ideia pq
'''
def fatprim(x):
    i=1
    p=x
    l=[]
    while p!=1:
        i+=1
        if p%i==0:
            l.append(i)
            p=p/i
        else:
            pass
    return l        
    
