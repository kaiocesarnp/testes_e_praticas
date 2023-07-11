import random 

print('Bem-vindo ao seu gerador de senhas')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('\nQuantidade de senhas para gerar: ')
number = int(number)

length = input('Quantidade de caracteres da senha: ')
length = int(length)

print('\nAqui estão suas senhas:')

for pwd in range(number):
   passwords = ''
   for c in range(length):
      passwords += random.choice(chars)
   print(passwords)