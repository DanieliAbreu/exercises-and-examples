#Laço FOR - Laço com contador e limite
_dias_da_semana = (1, 'Domingo ', 2, 'Segunda ', 3, 'Terça ',
                   4, 'Quarta ', 5, 'Quinta', 6, 'Sexta', 7, 'Sabado')

_dias_uteis = ('Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta')

_final_de_semana = ('Sabado ', 'Domingo')

#Exemplo 1
for i in _dias_da_semana:
    if type(i) != int:
       print(i)
print('Fim do Exempo 1')
print()
 
#Exemplo 2
for i in range(len(_dias_uteis)):
        print(i , _dias_uteis[i])
print('Fim do Exemplo 2')
print()
    
#Exemplo 3
for i , v in enumerate(_final_de_semana):
    print(i , v)
print('Fim do Exemplo 3')
print()
