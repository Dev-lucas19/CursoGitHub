# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Recebe uma string do usuário
texto = input("Digite uma string: ")
# Recebe um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))
# Repete a string o número de vezes informado
resultado = texto * numero
# Exibe o resultado
print("Resultado da repetição:", ' '.join([texto] * numero))