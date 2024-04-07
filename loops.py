#5. Crie uma função que imprime uma contagem de 0 a 20. Ao final faça um commit no GitHub.
#Exemplo de entrada: Nenhuma Exemplo de saída: 0 1 2

def imprimir_contagem():
    for i in range(21):
        print(i)

# Chamando a função para imprimir a contagem
imprimir_contagem()


#6. Crie uma função que imprime uma contagem de 0 até o número que o usuário digitou. 
#Exemplo de entrada: 3 Exemplo de saída:
#0 1 2 3  (um número embaixo do outro).

def imprimir_contagem(numero):
    for i in range(numero+1):
        print(i)

numero_digitado = int(input("Digite um número: "))
imprimir_contagem(numero_digitado)

