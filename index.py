import os
os.system('cls')

lista_nome = ["Eduardo", "Matheus" , 32, 18, "Guilherme", 13]
elem = "Guilherme"

def busca(lista: list, elemento: str):
    # Retorna o indice do elemento se ele estiver na lista ou None(vazio), caso o contrario
    return lista.index(elemento) if elemento in lista else None

indice = busca(lista_nome, elem)

print("O indice do elemento '{}' é {}.".format(elem, indice) if indice != None else "O elemento '{}' não se encontra na lista.".format(elem))
