def hannoing_iniciar(N,M=1,movtotal=0):
    a=list(range(N,0,-1))
    b=[0]*N
    c=[0]*N
    cestado(a,b,c,movtotal,M,N)
    return hanoi_resolver(a,b,c,movtotal,M,N)



def hanoi_resolver(a,b,c,movtotal,M,N):    
    if N%2 == 1:
        mov(a,c,N)
        movtotal+=1
        cestado(a,b,c,movtotal,M,N)
        if teste(a,b,c,N) == True:
            print('A solução demorou '+str(movtotal)+' Movimentos para ser concluida.')
            return
        
        mov(a,b,N)
        movtotal+=1
        cestado(a,b,c,movtotal,M,N)
        if teste(a,b,c,N) == True:
            print('A solução demorou '+str(movtotal)+' Movimentos para ser concluida.')
            return
        
        mov(b,c,N)
        movtotal+=1
        cestado(a,b,c,movtotal,M,N)
        if teste(a,b,c,N) == True:
            print('A solução demorou '+str(movtotal)+' Movimentos para ser concluida.')
            return

    else:
        mov(a,b,N)
        movtotal+=1
        cestado(a,b,c,movtotal,M,N)
        if teste(a,b,c,N) == True:
            print('A solução demorou '+str(movtotal)+' Movimentos para ser concluida.')
            return
        
        mov(a,c,N)
        movtotal+=1
        cestado(a,b,c,movtotal,M,N)
        if teste(a,b,c,N) == True:
            print('A solução demorou '+str(movtotal)+' Movimentos para ser concluida.')
            return
        
        mov(b,c,N)
        movtotal+=1
        cestado(a,b,c,movtotal,M,N)
        if teste(a,b,c,N) == True:
            print('A solução demorou '+str(movtotal)+' Movimentos para ser concluida.')
            return
    return hanoi_resolver(a,b,c,movtotal,M,N)

def cestado(a,b,c,movtotal,M,N):
    d = movtotal%M
    if d == 0:
        print('\n')
        for i in range(N-1,-1,-1):
            x='0'*(N-a[i])+a[i]*'#'+'|'+a[i]*'#'+'0'*(N-a[i])
            y='0'*(N-b[i])+b[i]*'#'+'|'+b[i]*'#'+'0'*(N-b[i])
            z='0'*(N-c[i])+c[i]*'#'+'|'+c[i]*'#'+'0'*(N-c[i])
            print(x+' '+y+' '+z)
        print('_'*(6*N+5))
        print('\n'+'Movimentos até o momento:  '+str(movtotal)+'\n')
    return 

def mov(x,y,N):
    for i in range(len(x)):
        if x[i] == 0:
            q=x[max(i-1,0)]
            qi=max(i-1,0)
            break
        else:
            q=x[-1]
            qi=-1
    for i in range(len(y)):
        if y[i] == 0:
            p=y[max(i-1,0)]
            pi=max(i-1,0)
            break
        else:
            p=y[-1]
            pi=-1
    if q > p and p != 0:
        return mov(y,x,N)
    
    if q > p and p == 0:
        x[qi]=0
        y[pi]=q
        return
    
    if q < p and  q == 0:
        return mov(y,x,N)
    if q < p :
        x[qi]=0
        y[pi+1]=q
        return
def teste(a,b,c,N):
    if c == list(range(N,0,-1)):
        return True
        
