#Estrutura de dados com chaves e valores , sendo as chaves definidas dentro do proprio
#dicionadio, os dicionários são criados com { }

_mes_do_ano = {'jan': 'Janeiro' , 'fev' : 'Fevereiro', 'mar' : 'Março', 'abr': 'Abril',
               'mai': 'Maio', 'jun' : 'Junho', 'jul' : 'Julho' , 'ago' : 'Agosto',
               'set': 'Setembro' , 'out': 'Outubro' , 'nov' : 'Novembro', 'dez' : 'Dezembro'}

#Exemplo 1
print(_mes_do_ano['jan'])

#Exemplo 2
print(_mes_do_ano.get('DEZ' , 'Mês não encontrado e/ou digitado errado'))

#Exemplo 3
print(_mes_do_ano.get('dez', 'Mês não encontrado e/ou digitado errado'))

#Exemplo 4 - Possibilidade de perguntar se a chave esta ou não no dicionário
if ('jan' in _mes_do_ano) == True:
    print('Mês cadastrado')
else:
    print('Mês não cadastrado')
print()
    
if ('JAN' in _mes_do_ano) == True:
    print('Mês cadastrado')
else:
    print('Mês não cadastrado')

#Exemplo 4

_lingua = {'br':'Portugues' , 'eua' : 'Ingles'}
print('Dicionário sem a espanha: ')
print(_lingua)
print()
print('Dicionario com a inclusão da espanha')
_lingua ['es'] = 'Espanhol'
print(_lingua.update())


#Interação com os dicionários

for _cha in _lingua:
    print(_cha.upper())
print()

for _chaves in _lingua.keys():
    print(_chaves.upper())
print()

for _valor in _lingua.values():
    print(_valor)
print()

for _chaves , _valor in _lingua.items():
    print(_chaves.upper(), _valor.upper())
print()

#Retirar um valor de um dicionário o .POP
print('Valor do item retirado do dinionário, ele apresenta o valor e não a chave:')
print(_lingua.pop('br'))
print()
print(_lingua)
print()

#Retirar um valor de um dicionário com o DEL
print('Valor do dicionário apagado com del não é mostrado:')
del _lingua['es']
print(_lingua)

