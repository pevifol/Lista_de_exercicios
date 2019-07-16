import os
from calcmat.py import *
from classe.py import *
arquivos = os.listdir("."+'/matrizes')

m_op={
    '1':a+b,#
    '2':a-b,#
    '3':a*b,#
    }
m_1m={
    '1':multi_esc(a)# [O overload de operador se encontra dentro dessa função)
    '2':trac(a)#
    '3':detm(a) # 
    '4':transpor(a.v) #
    }

m_mm={
    '1'
    '2'
    '3'
    '4'
    '5'
    '6'
    '7'
    '8'
    
def menu():
    a=input('''Olá! bem vindo ao menu da calculadora matricial. Por favor, escolha uma das seguintes opções:
1) Realizar Operação entre duas matrizes:
2) Realizar operação entre só uma matriz/ uma matriz e um numero escalar:
3) Manipular lista de matrizes/matrizes
4) Sair do menu:

''')
    if a=='4':
        return
    if a=='2':
        try:
            print('Matrizes disponíveis para a escolha:')
            for i in arquivos:
                c=str(arquivos.index(i)+1)+' - '+i
                print(c)
            a=input('Matriz escolhida: ')
            a=matriz(arquivos[a])
            b=input('''Operações disponíveis:
1) Multiplicar matriz por escalar
2) Calcular o traço da matriz (se ela for quadrada)
3) Calcular o determinante da matriz (se ela for triangular)
4) Fazer transposição da matriz!

''')           
            resultado=m_1m[b]
            return resultado
    
    if a=='1':
        c=input('''Operações disponíveis:
1)Soma de matrizes
2)Subtração de matrizes
3) Multiplicação de matrizes

''')
        try:
            print('Matrizes disponíveis para a escolha:')
            for i in arquivos:
                c=str(arquivos.index(i)+1)+' - '+i
                print(c)
            b=input('Matriz escolhida: ')
            b=matriz(arquivos[b])
            a=input('Matriz escolhida: ')
            a=matriz(arquivos[a])
            resultado = m_op[c]
            return resultado
        except:
            print("Um problema ocorreu. Tente novamente.")
    

