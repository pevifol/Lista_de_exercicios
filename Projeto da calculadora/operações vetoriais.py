import math
def escmult(): #Multiplica um vetor por um numero escalar qualquer 
    z=cvec1(N)
    c=int(input(Defina aqui o numero pelo qual você deseja multiplicar o vetor: ))
    for i in z:
        z[i]*=c
    return z
def prodint(z1,z2): #Calcula o produto interno entre 2 vetores.   
    z3=[]
    resul=0    
    for i in range(N):
        z3[i]=z1[i]*z2[i]
        resul+=z3[i]
    return resul
def sumvet(): #Calcula a soma vetorial de 2 vetores
    z1=cvec1(N)
    z2=cvec2(N)
    z3=[]
    for i in range(N):
        zr[i]=z1[i]+z2[i]
    return zr 
def modvet(z1): #Calcula o módulo de 1 vetor.  
    p=0
    for i in range(N):
        z1[i]=z1[i]**2
        p+=z1[i]    
   return math.sqrt(p)
def angevet(): #Calcula o angulo entre 2 vetores,e retorna em radianos.
    z1=cvec1(N)
    z2=cvec2(N)
    p=prodint(z1,z2)
    q=modvet(z1)+modvet(z2)
    teta= math.acos(p/q)
    return teta
def disvet(): #calcula a distância entre 2 vetores.  
    z1=cvec1(N)
    z2=cvec2(N)
    z3=[]
    r=0
    for i in range(N):
        z3[i]=z1[i]-z2[i]
        z3[i]=z3[i]**2
        r+=z3[i]
    return math.sqrt(r)  
def comblin(): #realiza a combinação linear de 2 vetores:
     z1=cvec1(N)
     z2=cvec2(N)
     z3=[]
     for i in range(N):
         z3[i]=z1[i]*z2[i]]
     return z3    
    
