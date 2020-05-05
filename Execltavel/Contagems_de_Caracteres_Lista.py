def contar_caracteres_string(a):
    
    caracter_ordenar = sorted(a)
    
    caracte_anterior = caracter_ordenar[0]
    contagem = 1
    
    for caracter in caracter_ordenar[1:]:
        if caracter == caracte_anterior:
            contagem += 1
        else:
            print(f'{caracte_anterior}:{contagem}')
            caracte_anterior= caracter
            contagem = 1
    print(f'{caracte_anterior}:{contagem}')
    
if __name__ == '__main__':
    contar_caracteres_string('inbu')
    print()
    contar_caracteres_string('banana')
    print()
