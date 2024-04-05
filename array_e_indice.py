#1. Crie uma função que declara um array com 4 nomes diferentes e imprime cada um deles um embaixo do outro. Ao final faça um commit no GitHub.

#Exemplo de entrada: Nenhuma Exemplo de saída:

#1-João 2-Maria 3-Fulano 4-Ciclano


lista_nomes = ['João', 'Maria', 'Fulano', 'Ciclano']

for i in range(4) :
    print(lista_nomes[i])
    

#2. Crie uma função que declara um array com 4 nomes diferentes e imprime o primeiro e último nome do array. 

#Exemplo de entrada : Nenhuma Exemplo de saída: 1-João 4-Beltrano

def imprimir_primeiro_e_ultimo_nome():
    # Declaração do array com os nomes
    nomes = ["João", "Maria", "Rute", "Miguel"]
    
    # Imprime o primeiro nome
    print(f"1-{nomes[0]}")
    
    # Imprime o último nome
    print(f"4-{nomes[3]}")

# Chamando a função para imprimir os nomes
imprimir_primeiro_e_ultimo_nome()

    
