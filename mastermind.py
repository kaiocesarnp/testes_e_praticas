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
