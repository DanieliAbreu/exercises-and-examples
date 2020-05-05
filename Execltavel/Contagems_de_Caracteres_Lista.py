def contar_caracteres_string(a):
    """ Função que conta caracteres de uma determinada string
       # >>> contar_caracteres_strig('Inbu')
        Ex:
        b: 1
        I: 1
        n: 1
        u: 1
    
       # >>> contar_caracteres_strig('Banana')
        a : 3
        b : 1
        n : 2
    :param a: String a ser contada
    """
    caracter_ordenar = sorted(a)
    caracte_anterior = caracter_ordenar[0]
    contagem = 1
    
    for caracter in caracter_ordenar[1:]:
        if caracter == caracte_anterior:
            contagem += 1
        else:
            print(f'{caracte_anterior }:{contagem}')
            caracte_anterior= caracter
            contador = 1
    print(f'{caracte_anterior }: {contagem}')
    
#if __name__ == '__main__':
contar_caracteres_strig('imbu')
print()
contar_caracteres_strig('banana')
print()
