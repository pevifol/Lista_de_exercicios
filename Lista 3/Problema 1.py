''' Q1 da lista 3: Subrotina da tabela ASCII'''
def printasci(inicio=32,fim=127,tampag=25):
    if inicio >= fim:
        return ('Defina um valor para início menor do que fim, por favor.')
    else:        
        while inicio < fim:
            print(
                '''+-----------+-----+-----+-----+-----+
|  Binário  | Oct | Hex | Dec | Chr |
+-----------+-----+-----+-----+-----+''')
            z=inicio+tampag
            if z>127:
                z=127
            for i in range(inicio,min(inicio+tampag,fim)):
                print('| {0} {1} | {2} |  {3} | {4} |  {5}  |'.format(bin(i)[2:].zfill(8)[:4],bin(i)[-4:],oct(i)[2:].zfill(3),hex(i)[2:],str(i).zfill(3),chr(range(32,128)[i%95])))
            print('+-----------+-----+-----+-----+-----+\n')
            inicio=inicio+tampag    
     
