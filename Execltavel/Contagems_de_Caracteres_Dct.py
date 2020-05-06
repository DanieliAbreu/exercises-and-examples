def contar_caracteres_Dct(a):

    """ Uma forma de impressão da contagem utilizano o dicionário
   resultado = {}
   
    for caracter in a:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter]=contagem
    return resultado

    """
    """ Outra forma de impressão de contagem utilziando o dicionário """
    resultado={}
    
    for caracter in a:
        resultado[caracter] = resultado.get(caracter, 0 ) + 1
        
    return resultado
    
if __name__ == '__main__':
    print(contar_caracteres_Dct('inbu'))
    print()
    print(contar_caracteres_Dct('banana'))
    print()
