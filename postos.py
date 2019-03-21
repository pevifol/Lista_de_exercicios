import random
def acharposto():
    coordenadas_de_x=[]
    coordenadas_de_y=[]
    p=0
    postos=[]
    n=1
    pi=float(input('digite a distância máxima do posto em relação a você em km: \n'))
    while p<12:
        p+=1
        x=random.randint(0,180)
        y=random.randint(0,180)
        coordenadas_de_x.append(x)
        coordenadas_de_y.append(y)
    q=float(input('Sua posição X num sistema de coordenadas de 0 a 180: '))    
    while n<90:
        if q not in range(181):
            print('Sua posição X está fora do limite do sistema. Digite ela novamente.')
            q=float(input('Sua posição X num sistema de coordenadas de 0 a 180: '))
        if q in range(181):
            break       
    a=float(input('Sua posição Y num sistema de coordenadas de 0 a 180: '))    
    while n<90:              
        if a not in range(181):
            print('Sua posição Y está fora do limite do sistema. Digite ela novamente.')
            q=float(input('Sua posição Y num sistema de coordenadas de 0 a 180: '))
        if a in range(181):
            break        
    for z in range(0,12):       
        ab=coordenadas_de_x[z]-q
        print(ab)
        ac=coordenadas_de_y[z]-a
        print(ac)
        ab=ab**2        
        ac=ac**2
        print(ab)
        print(ac)
        ad=ab+ac
        ad=ad**(0.5)
        print(ad)
        if ad < pi:
            postos.append('Posto '+str(z))       
        else:
            pass
    if postos == []:
        print('Infelizmente, não há postos perto o suficiente.')
    else:
        print(postos)

    

    
    
