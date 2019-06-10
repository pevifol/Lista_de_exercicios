def lmatriz(a="."):
    try:
        x=open(a,"r")
        z=x.read().split('\n')
        z[0]=z[0].split('')
        for i in range(1,len(z)):
            z[i]=z[i].split(',')
        x.close()   
    except FileNotFoundError:
        print('O arquivo não foi encontrado. Por favor, digite o nome/caminho correto para o arquivo.')
        return lmatriz(input())
    if len(z[0])!=2:
        raise IndexError('A matriz está no formato errado. A primeira linha deve conter dois numeros inteiros, respectivamente o numero de linhas e de colunas da matriz.')
    for i in range(1,len(z)):
        for q in range(z[0][1]):
            assert(1 in bool(type(z[i][q]==float))), "Um dos valores da matriz não é um ponto flutuante."
    if len(z)!=z[0][0]:
                   raise IndexError("O identificador de linhas da matriz está incorrreto.")
    for i in range(1,len(z)):
                   assert(1 in bool(len(z[i]==z[0][1]))),"O identificador de colunas da matriz está incorreto."
    return z               
 
