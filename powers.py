print("Defina quatro valores de poder:")
num_powers = 4
powers = []

for i in range(num_powers):
    power = int(input("Digite um valor para power: "))
    powers.append(power)

powers_sorted = sorted(powers)

print("Poderes em ordem crescente:", powers_sorted)


num_powers = 4: Define a variável num_powers com o valor 4, que representa o número de valores que serão inseridos para os poderes.

powers = []: Inicializa uma lista vazia chamada powers que será usada para armazenar os valores dos poderes.

for i in range(num_powers):: Inicia um loop que irá iterar 4 vezes, uma para cada valor de poder que o usuário precisa inserir.

power = int(input("Digite um valor para power: ")): Solicita ao usuário que digite um valor para o poder e o converte para um número inteiro usando int(). O valor digitado é armazenado na variável power.

powers.append(power): Adiciona o valor do poder à lista powers usando o método append(), para que seja armazenado para uso posterior.

powers_sorted = sorted(powers): A função sorted() é usada para ordenar os valores na lista powers em ordem crescente, e o resultado é armazenado na lista powers_sorted.

print("Poderes em ordem crescente:", powers_sorted): Imprime a frase "Poderes em ordem crescente:" seguida pelos valores dos poderes ordenados presentes na lista powers_sorted