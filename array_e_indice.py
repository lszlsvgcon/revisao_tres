#Lista de array sem estruturas de repetição.
#1. Crie uma função que declara um array com 4 nomes diferentes e imprime cada um deles um embaixo do outro. Ao final faça um commit no GitHub.
#Exemplo de entrada: Nenhuma Exemplo de saída:
#1-João 2-Maria 3-Fulano 4-Ciclano
##Alteração- foi retirado a estrutura de repetição for.

def imprime_nomes():
    # Declaração do array com 4 nomes diferentes
    nomes = ["João", "Maria", "Rute", "Miguel"]

    # Imprime cada nome um embaixo do outro
    print(f"1-{nomes[0]}")
    print(f"2-{nomes[1]}")
    print(f"3-{nomes[2]}")
    print(f"4-{nomes[3]}")

if __name__ == "__main__":
    imprime_nomes()

    
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

    
#3. Crie uma função que declara um array com 4 nomes diferentes e imprime o conteúdo do segundo e terceiro índice do array. 
#Exemplo de entrada: Nenhuma Exemplo de saída: 2-Maria 3-Fulano

def main():
    # Declaração do array com 4 nomes diferentes
    nomes = ["João", "Maria", "Rute", "Miguel"]

    # Imprime o conteúdo do segundo e terceiro índice
    print(f"2-{nomes[1]}")
    print(f"3-{nomes[2]}")

if __name__ == "__main__":
    main()


