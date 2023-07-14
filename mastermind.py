import random

num = random.randrange(1000, 10000)

n = int(input("Adivinhe o número de 4 dígitos:"))

if n == num:
    print("Ótimo! Você adivinhou o número em apenas 1 tentativa! Você é um gênio!")
else:
    ctr = 0
    while n != num:
        ctr += 1
        count = 0
        n = str(n)
        num = str(num)
        correct = ['X'] * 4

        for i in range(0, 4):
            if n[i] == num[i]:
                count += 1
                correct[i] = n[i]
        
        if count < 4 and count != 0:
            print("Não é exatamente o número. Mas você acertou", count, "dígito(s) corretamente!")
            print("Também estes números na sua entrada estavam corretos:")
            for k in correct:
                print(k, end=' ')
            print('\n')
            n = int(input("Digite sua próxima escolha de números: "))
        elif count == 0:
            print("Nenhum dos números na sua entrada corresponde.")
            n = int(input("Digite sua próxima escolha de números: "))

    if n == num:
        print("Você se tornou um gênio!")
        print("Levou apenas", ctr, "tentativas.")


#Explicação linha à linha:


# import random: Importa o módulo random, que permite gerar números aleatórios.

# num = random.randrange(1000, 10000): Gera um número aleatório entre 1000 e 9999 e o armazena na variável num.

# n = int(input("Adivinhe o número de 4 dígitos:")): Solicita ao usuário que insira um número de 4 dígitos e o converte em um número inteiro, armazenando-o na variável n.

# if n == num:: Verifica se o número digitado pelo usuário é igual ao número gerado aleatoriamente. Se forem iguais, executa o bloco de código abaixo.

# print("Ótimo! Você adivinhou o número em apenas 1 tentativa! Você é um gênio!"): Imprime a mensagem de parabéns, pois o usuário adivinhou o número em apenas uma tentativa.

# else:: Se o número digitado pelo usuário não for igual ao número gerado aleatoriamente, executa o bloco de código abaixo.

# ctr = 0: Inicializa a variável ctr como zero. Essa variável será usada para contar o número de tentativas.

# while n != num:: Inicia um loop que continua até que o número digitado pelo usuário seja igual ao número gerado aleatoriamente.

# ctr += 1: Incrementa o contador de tentativas em 1 a cada iteração do loop.

# count = 0: Inicializa a variável count como zero. Essa variável será usada para contar o número de dígitos corretos.

# n = str(n): Converte o número digitado pelo usuário em uma string para facilitar a comparação dos dígitos.

# num = str(num): Converte o número gerado aleatoriamente em uma string para facilitar a comparação dos dígitos.

# correct = ['X'] * 4: Cria uma lista chamada correct com quatro elementos, cada um contendo a letra 'X'. Essa lista será usada para exibir quais dígitos foram adivinhados corretamente.

# for i in range(0, 4):: Inicia um loop que percorre os dígitos do número (de 0 a 3).

# if n[i] == num[i]:: Verifica se o dígito atual da entrada do usuário é igual ao dígito correspondente do número gerado aleatoriamente.

# count += 1: Incrementa o contador de dígitos corretos em 1.

# correct[i] = n[i]: Atualiza a lista correct na posição i com o dígito correto.

# if count < 4 and count != 0:: Verifica se há dígitos corretos, mas não todos corretos.

# print("Não é exatamente o número. Mas você acertou", count, "dígito(s) corretamente!"): Imprime a mensagem informando quantos dígitos foram adivinhados corretamente.

# print("Também estes números na sua entrada estavam corretos:"): Imprime a mensagem indicando quais dígitos estavam corretos na posição correta.

# for k in correct: print(k, end=' '): Percorre a lista correct e imprime cada elemento separado por um espaço.

# n = int(input("Digite sua próxima escolha de números: ")): Solicita ao usuário que insira uma nova tentativa de adivinhar o número e converte a entrada em um número inteiro, atualizando a variável n.

# elif count == 0:: Verifica se nenhum dígito corresponde ao número gerado aleatoriamente.

# print("Nenhum dos números na sua entrada corresponde."): Imprime a mensagem informando que nenhum dígito corresponde ao número gerado aleatoriamente.

# n = int(input("Digite sua próxima escolha de números: ")): Solicita ao usuário que insira uma nova tentativa de adivinhar o número e converte a entrada em um número inteiro, atualizando a variável n.

# if n == num:: Verifica se o número digitado pelo usuário é igual ao número gerado aleatoriamente. Se forem iguais, executa o bloco de código abaixo.

# print("Você se tornou um gênio!"): Imprime a mensagem parabenizando o usuário por ter adivinhado o número corretamente.

# print("Levou apenas", ctr, "tentativas."): Imprime o número de tentativas que o usuário levou para adivinhar o número corretamente.
