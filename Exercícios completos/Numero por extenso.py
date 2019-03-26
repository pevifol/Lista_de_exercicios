'''
Programa feito por Ruan felipe da silva e sousa, aluno de matemática aplicada UFRJ, 2019.
Esse programa define a função extenso, que recebe um parametro x ( de até 5 algarismos)
e do tipo int e retorna sua escrita por extenso.
Eu acredito que este programa não tenha nenhum erro, mas é inviavel testar todos os 100.000
numeros. (de 1 a 99.999)
'''
def extenso(x):
    z=str(x)
    p=''
    if x<10000:
        z='0'+str(x)        
    if x<1000:
        z='00'+str(x)        
    if x<100:
        z='000'+str(x)           
    tup=tuple(z)   
    dict1 = {
        '0':'',
        '2':'Vinte e',
        '3':'Trinta e',
        '4':'Quarenta e',
        '5':'Cinquenta e',
        '6':'Sessenta e',
        '7':'Setenta e',
        '8':'Oitenta e',
        '9':'Noventa e',
        }
    dict1a = {
        '10':'Dez',
        '11':'Onze',
        '12':'Doze',
        '13':'Treze',
        '14':'Quatorze',
        '15':'Quinze',
        '16':'Dezesseis' ,       
        '17':'Dezessete',
        '18':'Dezoito',
        '19':'Desenove',
        }
    dict2a = {
        '0':'',
        '1':' mil ,',
        '2':' dois mil ,',
        '3':' três mil ,',  
        '4':' quatro mil ,',
        '5':' cinco mil ,',
        '6':' seis mil ,',       
        '7':' sete mil ,',
        '8':' oito mil ,',
        '9':' nove mil ,',
        }
    dict2b = {
        '0':'',
        '1':' um',
        '2':' dois',
        '3':' três',  
        '4':' quatro',
        '5':' cinco',
        '6':' seis',       
        '7':' sete',
        '8':' oito',
        '9':' nove',
        }
    dict2 = {
        '0':'',
        '1':' um',
        '2':' dois',
        '3':' três',  
        '4':' quatro',
        '5':' cinco',
        '6':' seis',       
        '7':' sete',
        '8':' oito',
        '9':' nove',
        }
    dict3= {
        '0':'',
        '1':'cento e ',
        '2':'duzentos e ',
        '3':'trezentos e ',  
        '4':'quatrocentos e ',
        '5':'quinhentos e ',
        '6':'seiscentos e ',       
        '7':'setecentos e ',
        '8':'oitocentos e ',
        '9':'novecentos e ',
        }
    dict4= {
        '0':'',        
        '2':'vinte e',
        '3':'trinta e',  
        '4':'quarenta e',
        '5':'cinquenta e',
        '6':'sessenta e',       
        '7':'setenta e',
        '8':'oitenta e',
        '9':'noventa e',
        }
    dict4a= {
        '0':'',        
        '2':'vinte',
        '3':'trinta',  
        '4':'quarente',
        '5':'cinquenta',
        '6':'sessenta',       
        '7':'setenta',
        '8':'oitenta',
        '9':'noventa',
        }
    if tup[0]=='1': #verifica o primeiro dígito, se for ígual a um, precisa utilizar nomes diferente        
        p=p+dict1a[tup[0]+tup[1]]
        p=p+' mil,'
        p=p+dict3[tup[2]]
        p=p+dict4[tup[3]]        
        p=p+dict2[tup[4]]+'.'
        return p
    if x<1000:
        p=p+dict1[tup[0]]
        p=p+dict2a[tup[1]]
        p=p+dict3[tup[2]]
        p=p+dict4a[tup[3]]
        p=p+dict2b[tup[4]]+'.'
        return p
    else:
        p=p+dict1[tup[0]]
        p=p+dict2a[tup[1]]
        p=p+dict3[tup[2]]
        p=p+dict4[tup[3]]
        p=p+dict2b[tup[4]]+'.'
        return p
    
        
