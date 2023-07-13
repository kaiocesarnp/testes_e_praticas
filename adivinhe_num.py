import random

def adivinhar(x):
    random_number = random.randint(1, x)
    adivinhar = 0
    while adivinhar != random_number:
        adivinhar = int(input(f'Adivinhe um número entre 1 e {x}: '))
        if adivinhar < random_number:
            print('Desculpe, adivinhe novamente. Muito baixo.')
        elif adivinhar > random_number:
            print('Desculpe, adivinhe novamente. Muito alto.')

    print(f'Yay, parabéns. Você adivinhou o número {random_number} corretamente!')

adivinhar(10)


#Explicação linha à linha:

#import random: Esta linha importa o módulo random, que permite gerar números aleatórios no Python.

#def adivinhar(x):: Essa linha define uma função chamada adivinhar que recebe um parâmetro x.

#random_number = random.randint(1, x): Esta linha gera um número aleatório entre 1 e o valor de x (fornecido como parâmetro) e o armazena na variável random_number.

#adivinhar = 0: Aqui, é definida uma variável chamada adivinhar e atribuído o valor 0.

#while adivinhar != random_number:: Este é um loop while (laço de repetição) que continuará sendo executado até que o valor de adivinhar seja igual a random_number.

#adivinhar = int(input(f'Adivinhe um número entre 1 e {x}: ')): Nesta linha, o usuário é solicitado a fornecer um número por meio da função 
		#input(), que é convertido em um número inteiro usando int() e atribuído à variável adivinhar.

#if adivinhar < random_number:: Esta linha verifica se o valor de adivinhar é menor que random_number.

#print('Desculpe, adivinhe novamente. Muito baixo.'): Se a condição anterior for verdadeira, essa mensagem será impressa, indicando que o palpite do usuário foi muito baixo.

#elif adivinhar > random_number:: Esta linha verifica se o valor de adivinhar é maior que random_number.

#print('Desculpe, adivinhe novamente. Muito alto.'): Se a condição anterior for verdadeira, essa mensagem será impressa, indicando que o palpite do usuário foi muito alto.

#print(f'Yay, parabéns. Você adivinhou o número {random_number} corretamente!'): Quando o usuário adivinhar corretamente o número, esta mensagem será impressa, mostrando o número correto que foi gerado aleatoriamente.

#adivinhar(10): Esta linha chama a função adivinhar e passa o valor 10 como argumento para definir o limite superior para adivinhar o número.

