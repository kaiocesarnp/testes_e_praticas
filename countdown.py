import time 

def countdown(t):
	while t:
	    mins, secs = divmod(t, 60)
	    timer = '{:02d}:{:02d}'.format(mins, secs)
	    print(timer, end="\r")
	    time.sleep(1)
	    t -= 1

	print('Fire in the hole, motherfucker!')

t = input('Enter the time in seconds: ')

countdown(int(t))

Explicação linha à linha:

#import time: Importa o módulo time do Python, que fornece funcionalidades relacionadas ao tempo.

#def countdown(t):: Define uma função chamada countdown que recebe um argumento t.

#while t:: Inicia um loop enquanto a variável t for verdadeira (diferente de zero).

#mins, secs = divmod(t, 60): Divide o valor de t por 60 e armazena o quociente em mins (minutos) e o resto em secs (segundos).

#timer = '{:02d}:{:02d}'.format(mins, secs): Formata as variáveis mins e secs para terem sempre dois dígitos, preenchendo com zero à esquerda, 
			#e as combina em uma string no formato "MM:SS". Essa string formatada é armazenada na variável timer.

#print(timer, end="\r"): Imprime a variável timer na tela, substituindo a linha anterior a cada nova iteração do loop.

#time.sleep(1): Pausa a execução do programa por 1 segundo.

#t -= 1: Decrementa o valor de t em 1.

#print('Fire in the hole, motherfucker!'): Após o loop terminar, imprime a mensagem "Fire in the hole, motherfucker!" na tela.

#t = input('Enter the time in seconds: '): Solicita ao usuário que insira um valor em segundos e armazena esse valor na variável t.

#countdown(int(t)): Chama a função countdown, passando o valor inteiro de t como argumento.


















