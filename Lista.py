#A criação da lista em Pytro é feita atravez dos []
#todos elementos de uma lista devem ser separados por ,
#dir(lista) - Serve para mostrar o help da lista

print([1,2,3,4])
print()

#Função range, serve para criar uma progração aritmética

#Nesse exmplo a lista vai ser impressa com 10 caracteres ,
#começando do 0 e terminando no 9.
_lista = list(range(10))
print(_lista)
print()

#Exemplo de lista com argumento inicial
_lista1 = list(range(1, 11))
print(_lista1)
print()

#Exemplo de lista com argumento incial 1 , final 9 e contando de 2 em 2
_lista2 = list(range(0, 11 , 2))
print(_lista2)
print()

#Exemplo de lista decrescente
_lista3 = list(range(10, 0, -2))
print(_lista3)
print()

#Metodos basicos do objeto lista
# 1 - .sort() - Ordena a lista
_lista3.sort()
print(_lista3)
print()

# 2 - .append() - Acrescenta elemento na lista
_lista2.append(12)
print(_lista2)
print()

# 3 - .pop() - Remove o ultimo elemento da lista e retorna o valore dele
print(_lista2.pop())
print()
print(_lista2)
print()

# 4 - .extend() - Permite acrescentar variso elementos ao final de uma lista
_lista2.extend([12,14])
print(_lista2)
print()

# 5 - + - Concatena uma lista utilziando o sinal de mais, dessa forma sera
# acrescentado ao final da lista os valores digitados após o +
print(_lista2+[16,18])
print()

# 6 - * - Multiplicando a lista pelo valor inteiro digitado após ela
print(_lista2*3)
print()

# 7 - .split() - Separando sctinges dentro de uma lista
_lista4 = 'Python Pro'.split()
print(_lista4)
print()

_lista4 = 'Python-pro'.split('-')
print(_lista4)
print()

# 8 - .join() - Junta palavras de uma lista
_lista5 = ['Pythron' , 'pro']
print('#'.join(_lista5) )
print()
