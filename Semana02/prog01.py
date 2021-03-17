#Autor: Igor Augusto
#Data: 16/03/2021

#Função printf que imprime este valor 'Hello Word' de texto na tela
print('Hello World')

#Declaração da variavel message, phyton não precisa de ponto e virgula no final 
#Pode-se usar aspas simples ou aspas duplas para strings, porém tome cuidado com o uso da aspas simples
message = 'Hello World'

#Para usar uma string com várias linhas, basta adicionar três aspas
String_Teste = """Olá mundo,
como vai?"""

#Para descobrir quantos caracteres tem em nossa string basta usar len
print(len(message))

#Para acessar uma posição da string basta utilizar o colchetes
print(message[0])

#Para imprimir varios caracteres de uma string baseada no indice indo de
#0 até 5, também posso deixar em branco [:5], ou [6:] vai pegar a parte
#final da string
print(message[0:5])

#Irá imprimir todos os caracteres da string em letra minuscula
print(message.lower())

#Irá imprimir todos os caracteres da string em letra maiuscula
print(message.upper())

#Irá contar na string quantas vezes aparece o argumento
print(message.count('Hello'))

#Irá verificar na string onde começa o argumento inserido
#Neste caso será 6, pois é na posição 6 que começa o argumento inserido
print(message.count('World'))

#Substituição de caracteres numa string
message = message.replace('World','Universe')
print(message)

#Concatenação de strings
new_message_2 = message + ',' + String_Teste
print(new_message_2)

#Para lidar com strings também temos essa opção utilizando o string f
message2 = f'{message},{new_message_2}. Welcome!'
print(message2)

#Para sabermos os atributos e metodos de uma variavel
print(dir(message))

#Para sabermos vomo utilizar os atributos e metodos de uma variavel
print(help(string))

#Para sabermos vomo utilizar os atributos e metodos de uma variavel do tipo string em especifico
print(help(str.lower)
