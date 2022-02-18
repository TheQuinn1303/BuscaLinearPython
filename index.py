import os 
os.system('cls')

def busca(lista, elemento):
    """Retorna o indice do elemento se ele estiver na lista ou None(vazio), caso o contrario"""
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return None
    
lista_nome = ["Eduardo", "Matheus" , 32, 18, "Guilherme", 13]
elem = "Guilherme"

indice = busca(lista_nome,elem)
if indice is not None:
    print("o indice do elemento {} é {}". format(elem,indice))
else:
    print("O elemento {} não se encontra na lista".format(elem))
