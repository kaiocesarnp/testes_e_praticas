print("Defina quatro valores de poder:")
num_powers = 4
powers = []

for i in range(num_powers):
    power = None
    while power is None or power < 0 or power > 9:
        power = int(input("Digite um valor para power (entre 0 e 9): "))
        if power < 0 or power > 9:
            print("Valor inválido! O valor do poder deve estar entre 0 e 9.")

    powers.append(power)

powers_sorted = sorted(powers)

print("Poderes em ordem crescente:", powers_sorted)

#Explicação linha à linha:

#print("Defina quatro valores de poder:"): Exibe uma mensagem para o usuário solicitando a definição de quatro valores para os poderes.

#num_powers = 4: Define a variável num_powers com o valor 4, que representa o número de valores de poder que o usuário deve inserir.

#powers = []: Cria uma lista vazia chamada powers para armazenar os valores dos poderes.

#for i in range(num_powers):: Inicia um loop que irá iterar 4 vezes, uma vez para cada valor de poder que o usuário precisa inserir.

#power = None: Inicializa a variável power com o valor None, que representa a ausência de um valor válido.

#while power is None or power < 0 or power > 9:: Inicia um loop que continua até que um valor válido para o poder seja fornecido. O loop verifica se power é None (ou seja, sem valor) ou se está fora do intervalo de 0 a 9.

#power = int(input("Digite um valor para power (entre 0 e 9): ")): Solicita ao usuário que insira um valor para o poder e converte o valor fornecido em um número inteiro usando a função int().

#if power < 0 or power > 9:: Verifica se o valor do poder está fora do intervalo de 0 a 9.

#print("Valor inválido! O valor do poder deve estar entre 0 e 9."): Exibe uma mensagem de erro informando que o valor do poder deve estar entre 0 e 9.

#powers.append(power): Adiciona o valor do poder à lista powers usando o método append(), para que seja armazenado para uso posterior.

#powers_sorted = sorted(powers): Cria uma nova lista chamada powers_sorted com os valores dos poderes ordenados em ordem crescente.

#print("Poderes em ordem crescente:", powers_sorted): Exibe uma mensagem seguida pelos valores dos poderes ordenados presentes na lista powers_sorted.

