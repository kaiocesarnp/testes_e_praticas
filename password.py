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

#Explicação linha à linha:

#import random: Essa linha importa o módulo random, que contém funções relacionadas à geração de números aleatórios.

#print('Bem-vindo ao seu gerador de senhas'): Essa linha imprime uma mensagem de boas-vindas para o usuário.

#chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789': 
	#Aqui é definida uma string chamada chars, que contém todos os caracteres que podem ser usados para gerar as senhas. 
	   #Esses caracteres incluem letras minúsculas, letras maiúsculas, números e alguns caracteres especiais.

#number = input('\nQuantidade de senhas para gerar: '): Essa linha solicita ao usuário que digite a quantidade de senhas que deseja gerar e armazena o valor digitado na variável number.

#number = int(number): Aqui, o valor digitado pelo usuário é convertido para um número inteiro, pois a função input() retorna uma string.

#length = input('Quantidade de caracteres da senha: '): Semelhante à linha anterior, essa linha solicita ao usuário que digite o comprimento desejado para cada senha e armazena o valor digitado na variável length.

#length = int(length): O valor digitado pelo usuário é convertido para um número inteiro.

#print('\nAqui estão suas senhas:'): Essa linha imprime uma mensagem para indicar que as senhas serão exibidas a seguir.

#for pwd in range(number):: Aqui começa um loop que irá gerar o número especificado de senhas. O loop será executado number vezes.

#passwords = '': A variável passwords é inicializada como uma string vazia, onde a senha gerada será armazenada.

#for c in range(length):: Um segundo loop é iniciado para gerar cada caractere da senha. O loop será executado length vezes.

#passwords += random.choice(chars): A cada iteração do segundo loop, um caractere aleatório é escolhido da string chars usando a função random.choice(), e adicionado à variável passwords.

#print(passwords): Após o segundo loop, a senha gerada é impressa na tela.