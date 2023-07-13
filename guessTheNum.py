import random

def adivinhar(x):
    random_number = random.randint(1, x)
    adivinhar= 0
    while adivinhar != random_number:
        adivinhar = int(input(f'Adivinhe um número entre 1 e {x}: '))
        if adivinhar < random_number:
            print('Desculpe, adivinhe novamente. Muito baixo.')
        elif adivinhar > random_number:
            print('Desculpe, adivinhe novamente. Muito alto.')

    print(f'Yay, parabéns. Você adivinhou o número {random_number} corretamente!')

adivinhar(10)
