#A criaçào de uma Tupla em Pytho  é feita com os ()
#devendo ser separadas por " , " - Virgula
#A tupla é imutavel, não é possivel inserir ou remover elementos de uma tupla

tpl = (1,2,3,4)
print(tpl)
print(type(tpl))
print()

#Outra forma de criar uma tupla
print('Outra forma de criar uma tupla é usando a função "tuple" :')
print(tuple(range(5)))
print()

#Exemplos de uso de uma tupla
print('Dias uteis da semana : ')
_dias_util_da_semana = ( 2 , 'Segunda', 3 , 'Terça', 4 ,'Quarta', 5, 'Quinta', 6 , 'Sexta')
print(_dias_util_da_semana)
print()

print('Final de semana')
_fim_de_semana = ( 7, 'Sabado' , 1 , 'Domingo')
print(_fim_de_semana)
print()

print('Dias da Semana :')
print(_fim_de_semana + _dias_util_da_semana)
print()

#len - Retorna a quantidade de index de uma tupla
print('Quantidade de index da tupla "_dias_util_da_semana":')
print((len(_dias_util_da_semana)))
print()

#Selecionando o dia expecifico da semana utiliando o idece
_dai1 = _dias_util_da_semana[0]
print('Primeiro indice da tupla "_DIas_util_da_semana" : ')
print(_dai1)
print()
_dai1 = _dias_util_da_semana[1]
print('Segundo indice da tupla "_Dias_util_da_semana" : ')
print(_dai1)
print()

#slaice - Exemplos de possibilidades de utilização do fatiamento
print('Fatia')
_dia_fatiado = _fim_de_semana[-1:len(_fim_de_semana)] + _dias_util_da_semana[1:10:2] + _fim_de_semana[-3:len(_fim_de_semana)-2]
print(_dia_fatiado)
