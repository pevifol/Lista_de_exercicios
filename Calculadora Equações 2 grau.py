'''O meu primeiro programa na aula de topico de matemática aplicada A!
Aluno: Ruan felipe da silva e sousa.
DRE: 119041454.
Esse programa define e executa uma função que pergunta e calcula as raízes
de uma equação do segundo grau, informando casos onde ambas as raízes são iguais
14 de março de 2019.
'''
def calceq2():
    a=float(input("Qual é o valor do primeiro coeficiente? (a): "))
    b=float(input("Qual é o valor do segundo coeficiente? (b): "))
    c=float(input("Qual é o valor do terceiro coeficiente? (c): "))
    D=b**2-4*a*c
    xp=-b+D**(0.5)
    xpq=xp/2
    xq=-b-D**(0.5)
    xqp=xq/2
    oneraiz='Essa função tem duas raízes, mas elas são as mesmas e iguais a: '+str(xpq)
    semraiz='Essa função não tem raízes reais.'
    result='As raízes são '+str(xqp)+'e '+str(xpq)
    if D < 0:
        return print(semraiz)
    elif D==0:
        return print(oneraiz)
    else:
        return print(result)

calceq2()
