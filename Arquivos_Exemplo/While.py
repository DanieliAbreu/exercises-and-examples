# Exemplos do laço While em Python
# esse taço tem de se ter cuidado ao utilizaar
# por se tratar de um laço infinito uma vez que
# se a informação for sempre verdadeira ele fica
# no laço até o sistema ser finalizado
_dias_da_semana = (1, 'Domingo ', 2, 'Segunda ', 3, 'Terça ',
                   4, 'Quarta ', 5, 'Quinta', 6, 'Sexta', 7, 'Sabado')
_dias = 1

while _dias < len(_dias_da_semana):
    print(_dias_da_semana[_dias])
    _dias += 2
