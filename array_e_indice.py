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


#4. Crie uma função que pede 3 nomes de alimentos digitado pelo usuário e substitui os elementos do array [“Macarrão”, “Pepino”, “Batata”] com esses 3 alimentos. Imprima o nome dos alimentos um abaixo do outro. 
#array_inicial = [“Macarrão”, “Pepino”, “Batata”]
#Exemplo de entrada: Arroz, Feijão, Farinha Exemplo de saída: 1 – Arroz 2 - Feijão 3 – Farinha


def substituir_alimentos():
    # Lê os 3 nomes de alimentos digitados pelo usuário
    alimento1 = input("Digite o primeiro alimento: ")
    alimento2 = input("Digite o segundo alimento: ")
    alimento3 = input("Digite o terceiro alimento: ")

    # Cria o array inicial
    array_inicial = ["Macarrão", "Pepino", "Batata"]

    # Substitui os elementos do array com os alimentos digitados
    array_inicial[0] = alimento1
    array_inicial[1] = alimento2
    array_inicial[2] = alimento3

    # Imprime os nomes dos alimentos um abaixo do outro
    print(array_inicial[0])
    print(array_inicial[1])
    print(array_inicial[2])

# Chama a função
substituir_alimentos()

