%matplotlib inline
import mathplotlib.pyplot as plt
import pandas as pd
dado=pd.read_csv(input('Digite aqui o path para o arquivo: '),engine='c',encoding="latin1",sep=";")
#Código originalmente testado somente com 300.000 linhas, devido a incapacidade do jupyter de utilizar o banco de dados inteiro.
#(O jupyter crashava repetidamente na hora de fazer os gráficos utilizando o conjunto de dados inteiro)
#Isso significa que algumas excessões provavelmente não vão poder ser tratadas, justamente pois elas não aconteceram
#durante o desenvolvimento :/ Tentamos remediar isso por meio do leia-me, mas ele não lista todas as possibilidades
#nos campos.
dado=dado[dado.DS_FAIXA_ETARIA != "Inválido"]
dado=dado[dado.SG_UF != 'ZZ']
dado=dado[dado.SG_UF != 'VT']
dado=dado[dado.SG_UF != 'BR']
dado=dado[dado.DS_GENERO != "NÃO INFORMADO"]
dado=dado[dado.DS_GRAU_ESCOLARIDADE != "NÃO INFORMADO"]
#Todas os "problemas" encontrados durante o teste.
a=dado.groupby(['DS_FAIXA_ETARIA','DS_GENERO']).sum().unstack().plot(kind='bar',y='QT_ELEITORES_PERFIL',title='Gráfico Faixa etária x Eleitores')
a.set_xlabel("Faixa etária")
a.set_ylabel("N° de eleitores")
plt.savefig('gráficofxetaria.png')

b=dado.groupby(['SG_UF','DS_GENERO']).sum().unstack().plot(kind='barh',y='QT_ELEITORES_PERFIL',title='Gráfico UF x Eleitores')
b.set_xlabel("Unidade Federativa")
b.set_ylabel("N° de eleitores")
plt.savefig('gráficogenero.png')

c=dado.groupby(['DS_GRAU_ESCOLARIDADE','DS_GENERO']).sum().unstack().plot(kind='bar',y='QT_ELEITORES_PERFIL',title='Gráfico Escolaridade x Eleitores')
c.set_xlabel("Grau de escolaridade")
c.set_ylabel("N° de eleitores")
plt.savefig('gráficoescola.png')
