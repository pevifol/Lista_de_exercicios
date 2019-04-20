'''
Este é o projeto da calculadora vetorial, idealizada e criada por mim, Ruan felipe da silva e sousa, e meus companheiros, Matheus Moreira do Nascimento, Felipe Rodrigues Ribeiro e Igor torres.

A base da calculadora são as funções cvec1() e cvec(), que criam vetores, aqui definidos por uma lista, que são usados dentro das funções.
O resto da calculadora é divida em 3 módulos, as funções menu(), onde a calculadora se inicia, a função opc(), onde encontramos as opções da calculadora, e a função opv(), onde encontramos as
operações, de fato.
'''
import math
N=3 #tamanho comum do vetor. Utilizar isso em while loops,e alterar utilizando as opções.
z=2 #Numero que indica se o programa guarda o resultado da ultima conta ou não. (1 = ligado, 2 = desligado, 3 = guarda o resultado da ultima conta e soma ao resultado anterior.)
resultadof='' #Variavel global que armazena o resultado da ultima conta, e utiliza para realizar outras operações.

def menu():
     s=str(input(
         '''
              _________        .__               .__              .___                                  __               .__       .__             
          \_   ___ \_____  |  |   ____  __ __|  | _____     __| _/________________    ___  __ _____/  |_  ___________|__|____  |  |            
  ______  /    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \   / __ |/  _ \_  __ \__  \   \  \/ // __ \   __\/  _ \_  __ \  \__  \ |  |     ______ 
 /_____/  \     \____/ __ \|  |_\  \___|  |  /  |__/ __ \_/ /_/ (  <_> )  | \// __ \_  \   /\  ___/|  | (  <_> )  | \/  |/ __ \|  |__  /_____/ 
           \______  (____  /____/\___  >____/|____(____  /\____ |\____/|__|  (____  /   \_/  \___  >__|  \____/|__|  |__(____  /____/          
                  \/     \/          \/                \/      \/                 \/             \/                          \/                
    Bem vindo a calculadora vetorial! Escolha uma opção para continuar, ou digite SAIR para sair!
    1) Operações vetoriais 
    2) Configurações da calculadora \n'''))
     
     if type(s)== type(''):
          s=str.lower(s)
        
     if s not in ['2','1','sair']:
          print('\nOpção inválida, tente novamente.')
          menu() # Recursão para reiniciar o programa.
        
     if s == '1':
          opv()
        
     if s == '2':          
          opc()
        
     if s == 'sair':
          print('Programa encerrando.')
          return


''' Função Criar vetor - Essa função utiliza uma parametro N para criar um vetor de N coordenadas.
O resultado é uma lista.'''
def cvec1(x):     
     l=[]
     p=0
     while p != x:
          c=int(input('Digite o valor da '+str(p+1)+'° coordenada do 1° vetor.'))
          if type(c) != type(2):
               print('Valor inválido, digite novamente.')
               pass
          else:
               p+=1
               l.append(c)     
     print(l)
     return l       
def cvec2(x):
    q=[]
    p=0
    while p != x:         
         c=int(input('Digite o valor da '+str(p)+'° coordenada do 1° vetor.'))
         if type(c) != type(2):
              print('Valor inválido, digite novamente.')
              pass
         else:
              p+=1
              q.append(c)
    print(q)         
    return q

'''Menu de configurações da calculadora. '''
def opc():
     opc=input('~~Configuração da calculadora~~ \n1) Alterar a dimensão padrão dos vetores \n2) Memorizar resultados anteriores\n')
     if opc not in ['1','2','3']:
          print('\nOpção invalida, tente novamente.')
          opc()
     if opc == '1':
          p=int(input('\nDefina o tamanho padrão dos vetores: \n'))
          global N
          N=p
          menu()
     if opc == '2':
          global z
          if z == 1:
               print('\nMemorização de resultados anteriores desligada.')               
               z = 2
               menu()
          if z == 2:
               print('\nMemorização de resultados anteriores ligada.')               
               z = 1
               menu()
          else:
               print('what even está acontecendo')

'''Módulo das operações''' 

def escmult():
     global resultadof
     if resultadof != '':
          if type(resultadof)==type([]):
               z=resultadof
               c=int(input('Defina aqui o numero pelo qual você deseja multiplicar o vetor: '))
               za=[x*c for x in z]                   
               return za
          else:
               z=cvec1(N)
               c=resultadof
               za=[x*c for x in z]                   
               return za                 
     else:          
          z=cvec1(N)
          c=int(input('Defina aqui o numero pelo qual você deseja multiplicar o vetor: '))
          za=[x*c for x in z]          
          return za
          

def prodint(z1,z2): #Calcula o produto interno entre 2 vetores.   
    z3=[0]*N
    resul=0
    global resultadof
    for i in range(N):
        z3[i]=z1[i]*z2[i]
        resul+=z3[i]
    return resul

def sumvet(): #Calcula a soma vetorial de 2 vetores
     zr=[0]*N
     global resultadof
     if resultadof != '' and z==1:
          if type(resultadof)==type([]):
               z1=resultadof
               z2=cvec2(N)
               for i in range(N):
                    zr[i]=z1[i]+z2[i]
               return zr
          else:
               print('Não podemos realizar soma vetorial com um valor escalar.')
               menu()          
     else:
          z1=cvec1(N)
          z2=cvec2(N)    
          for i in range(N):
               zr[i]=z1[i]+z2[i]
          return zr       
def modvet(z1): #Calcula o módulo de 1 vetor.
     p=0
     global resultadof
     if resultadof != '' and z==1:
          if type(resultadof)==type([]):
               z2=resultadof
               for i in range(N):
                    z2[i]=z2[i]**2
                    p+=z2[i]
               return math.sqrt(p)     
          else:
               return resultadof
     else:          
          for i in range(N):
               z1[i]=z1[i]**2
               p+=z1[i]
          return math.sqrt(p)     
     

def angevet():#Calcula o angulo entre 2 vetores,e retorna em radianos.
     global resultadof
     if resultadof != '' and z==1:
          if type(resultadof)==type([]):
               z1=resultadof
               z2=cvec2(N)
               p=prodint(z1,z2)
               q=modvet(z1)*modvet(z2)
               teta= math.acos(p/q)
               return teta
          else:
               z1=[0]*N
               z1[0]=resultadof               
               z2=cvec2(N)
               p=prodint(z1,z2)               
               q=modvet(z1)*modvet(z2)
               teta= math.acos(p/q)
               return teta
     else:
          z1=cvec1(N)
          z2=cvec2(N)
          p=prodint(z1,z2)
          print(p)
          q=modvet(z1)*modvet(z2)
          print(q)
          teta= math.acos(p/q)
          return teta

def disvet():#calcula a distância entre 2 vetores.
     global resultadof
     z3=[]*N
     r=0
     if resultadof != '' and z==1:
          if type(resultadof)==type([]):
               z1=resultadof
               z2=cvec2(N)               
               for i in range(N):
                    z3[i]=z1[i]-z2[i]
                    z3[i]=z3[i]**2
                    r+=z3[i]
               return math.sqrt(r)
          else:
               z1=[0]*N
               z1[0]=resultadof
               z2=cvec2(N)
               z3=[]
               r=0
               for i in range(N):
                    z3[i]=z1[i]-z2[i]
                    z3[i]=z3[i]**2
                    r+=z3[i]         
               return math.sqrt(r)
     else:
          z1=cvec1(N)
          z2=cvec2(N)          
          for i in range(N):
               z3[i]=z1[i]-z2[i]
               z3[i]=z3[i]**2
               r+=z3[i]
               return math.sqrt(r)
          
def comblin(): #realiza a combinação linear de 2 vetores:
     global resultadof
     z3=[0]*N
     if resultadof != '' and z==1:
          if type(resultadof)==type([]):
               z1=resultadof
               z2=cvec2(N)
               for i in range(N):
                    z3[i]=z1[i]*z2[i]
               return z3
          else:               
               z1=[0]*N
               z1[0]=resultadof
               z2=cvec2(N)
               for i in range(N):
                    z3[i]=z1[i]*z2[i]
               return z3
     else:
          z1=cvec1(N)
          z2=cvec2(N)
          for i in range(N):
               z3[i]=z1[i]*z2[i]
          return z3    
    
def opv():
     global resultadof
     opv=int(input('''
~~Operações vetoriais~~
1) Soma vetorial
2) Multiplicação de vetor por numero escalar
3) Combinação linear de 2 vetores
4) Norma  Vetorial
5) Produto interno
6) Angulo entre os vetores \n'''))
    
     if opv == 1:
          a=sumvet()
          print('O resultado da operação é: '+str(a))          
          resultadof=a
          menu() 
     
     if opv == 2:
          b=escmult()
          print('O resultado da operação é: '+str(b))               
          resultadof=b
          menu()  
    
     if opv == 3:
          c=comblin()
          print('O resultado da operação é: '+str(c))     
          resultadof=c
          menu()
          
     if opv == 4:
          z1=cvec1(N)
          d=modvet(z1)
          print('O resultado da operação é: '+str(d))     
          resultadof=d
          menu()
     
     if opv == 5:
          if resultadof!='' and z1==1:
               if type(resultadof)==type([]):
                    z1=resultadof
                    z2=cvec2(N)
                    e=prodint(z1,z2)
                    resultadof=e
                    print('O resultado da operação é: '+str(e))
                    menu()
               else:
                    z1=[0]*N
                    z1[0]=resultadof
                    z2=cvec2(N)
                    f=prodint(z1,z2)               
                    resultadof=f
                    print('O resultado da operação é: '+str(f))
                    menu()
          else:
               z1=cvec1()
               z2=cvec2()
               g=prodint(z1,z2)          
               resultadof=g
               print('O resultado da operação é'+str(g))
               menu()                
     if opv == 6:
          h=angevet()
          print('O resultado da operação é: '+str(h))
          resultadof=h
          menu()        

        
