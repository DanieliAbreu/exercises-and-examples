#Uma função no python deve serguir as seguintes regras:
#Nomes das variaveis e das funções devem ser semrpe iniciado com letras minusculas
#e se for necessário ter nomes compostos deve ser separados po _ Underline

#Exemplo para definir uma função
def nome_funcao_sem_retorno():
    pass

def nome_funcao_com_retorno():
    return 'Olá Mundo!'

if __name__ == '__main__':
    _funcao1 = nome_funcao_sem_retorno()
    _funcao2 = nome_funcao_com_retorno()
    print('Função sem retorno')
    print(type(_funcao1))
    print()
    print('Função com retorno ')
    print(_funcao2)
    print()

#Parametros de funções
def ola(_nome):
    return f'Olá {_nome}'

if __name__ == '__main__':
    print(ola('Alex'))

#Exemplo de função com mais de um parametro
def ola_dois_parametors(_nome, _sobrenome):
    return f'Olá Sr. {_nome} {_sobrenome}'

if __name__ == '__main__':
    print('Função com dois parametros')
    print(ola_dois_parametors('Alex', 'Oliveira'))

#Parâmetros Variáveis
def soma(*args):
    _aux = 0 # Valor para guardar os valores das parcelas
    for valor in args:
        _aux += valor
    return _aux

if __name__ == '__main__':
    #Passando apenas um valor
    print(soma(2))

    #Passando dois valores
    print(soma(2,4))

    #Passando tres valores
    print(soma(2,4,10))

#Função com varios parametros , definida como dicionário
def func_dic(**kwargs):
    print(kwargs)

if __name__ == '__main__':
    #Passando valor para a função
    func_dic(nome = 'Alex')
