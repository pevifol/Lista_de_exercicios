''' Módulo de menu'''
def menu(): #comando inicial das funções, onde cada variavel fica armazenada.
    x=3 #tamanho comum do vetor. Utilizar isso em while loops,e alterar utilizando as opções.
    z=1 #Numero que indica se o programa guarda o resultado da ultima conta ou não. (1 = ligado, 2 = desligado, 3 = guarda o resultado da ultima conta e soma ao resultado anterior.)
    menua()
def menua(): #Menu inicial concluido
    s=input('''
              _________        .__               .__              .___                                  __               .__       .__             
          \_   ___ \_____  |  |   ____  __ __|  | _____     __| _/________________    ___  __ _____/  |_  ___________|__|____  |  |            
  ______  /    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \   / __ |/  _ \_  __ \__  \   \  \/ // __ \   __\/  _ \_  __ \  \__  \ |  |     ______ 
 /_____/  \     \____/ __ \|  |_\  \___|  |  /  |__/ __ \_/ /_/ (  <_> )  | \// __ \_  \   /\  ___/|  | (  <_> )  | \/  |/ __ \|  |__  /_____/ 
           \______  (____  /____/\___  >____/|____(____  /\____ |\____/|__|  (____  /   \_/  \___  >__|  \____/|__|  |__(____  /____/          
                  \/     \/          \/                \/      \/                 \/             \/                          \/                
    Bem vindo a calculadora vetorial! Escolha uma opção para continuar, ou digite SAIR para sair!
    1) Operações vetoriais 
    2) Configurações da calculadora ''')
    s=str.lower(s)
    if s not in ['2','1','sair']:
        print('\nOpção inválida, tente novamente.')
        menua() # Recursão para reiniciar o programa.
    if s == '1':        
        opv()
    if s == '2':
        opc()
    if s == 'sair':
        print('Programa encerrando.')
        return

def opc():
    #Menu de configuração das calculadoras.
    opc=input('~~Configuração da calculadora~~ \n1) Alterar a dimensão padrão dos vetores \n2) Memorizar resultados anteriores \n3) Acumular resultado vetorial')
    if opc not in ['1','2','3']:
        print('\nOpção invalida, tente novamente.')
        opc()# Recursão para reinciar o programa.
    if opc == '1':
        p=input('\nDefina o tamanho padrão dos vetores: \n')
        x=p
        menua()
    if opc == '2':
        if z == 1:
            print('\nMemorização de resultados anteriores desligada.')
            z = 2
            menua()
        if z == 2:
            print('\nMemorização de resultados anteriores ligada.')
            z = 1
            menua()
        else:
            print('\nMemorização de resultados anteriores ligada, e acumulo vetorial desligado.')
            z = 1
            menua()               
    if opc == '3':
            print('\nacumulo de resultado vetorial ligado, junto com memorização de resultados anteriores.')
            z=3
            menua()    
def opv():
    opv=input('''
~~Operações vetoriais~~
1)Soma vetorial
2) Multiplicação de vetor por numero escalar
3) Combinação linear de 2 vetores
4) Norma Vetorial
5) Produto interno
6) Angulo entre os vetores''')
    if opv == 1: #Definir todas essas funções. Cada um fica responsável por uma parte. Eu (Ruan felipe) cuido de ""costurar"" isso de forma decente. Pelo amor de deus cooperem.
        somavet()
    if opv == 2:
        multescvet()
    if opv == 3:
        comblinvet()
    if opv == 4:
        normvet()
    if opv == 5:
        intprod()
    if opv == 6:
        ang2vet()
    
