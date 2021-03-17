#Autor: Igor Augusto
#Data: 16/03/2021

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

#Aritmética de divisão
print(3/2)

#Aritmética de pegar o resto inteiro da divisão
print(3//2)

#Utilização de parenteses para ordenar a as operações aritméticas
#Resultado será 7
print(3*2+1)

#Resultado será 9
print((2+1)*3)

#Incrementar uma variável
num = 1

num +=1
print (num) #resultado será 2

#Função abs = valor absoluto de um número
print(abs(-3)) #resultado será 3

#Função round = arredonda o número || pode-se informar a quantidade de casas para arredondamento
print(round(3.75)) #resultado será 4
print(round(3.75,1)) #resultado será 3.8

#--------- Operadores Lógicos ------------
num_1 = 3
num_2 = 2

#Vai verificar se num1 é igual ao num2, caso verdade True, caso falso False
print(num_1 == num_2) #resultado será False

#Vai verificar se num1 é diferente do num2, caso verdade True, caso falso False
print(num_1 != num_2) #resultado será True

#Vai verificar se num1 é maior do num2, caso verdade True, caso falso False
print(num_1 > num_2) #resultado será True

#Vai verificar se num1 é menor do num2, caso verdade True, caso falso False
print(num_1 < num_2) #resultado será False

#Converter strings de textos em números
#String no formato de texto
num_3 = '100'
num_4 = '200'

#Convertendo a string em inteiro
num_3 = int(num_3)
num_4 = int(num_4)

print(num_3 + num_4)
