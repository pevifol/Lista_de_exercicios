'''
Este programa define uma função chamada primul, que utiliza o parametro x
e retorna os primeiros X multiplos de 7, e os primeiros X multiplos de 5,
no formato de lista.
Em seguida, o programa pergunta educadamente, e executa o primul(x) até o valor digitado.
'''
def primul(x):
    
    z=x+1
    list5=[]
    list7=[]
    for p in range(z):
        q=1
        q=5*p
        m=1
        m=7*p
        if q==0:
            pass
        else:
            list5.append(q)
            list7.append(m)      
    list5.sort()
    list7.sort()
    print('Os primeiros '+str(x)+' multiplos de 5 são:')
    print(list5)
    print('Os primeiros '+str(x)+' multiplos de 7 são:')
    print(list7)
    
def main()
    q=float(input(Defina até que multiplo de 5 e 7 você deseja saber, por favor.))
    primul(q)
