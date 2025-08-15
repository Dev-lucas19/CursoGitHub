# Vamos testar se uma palavra é um palíndromo, utilizando manipulação de strings e condicionais.

# Recebe uma palavra do usuário
palavra = input("Digite uma palavra: ")
# Verifica se a palavra é igual à sua reversa
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")