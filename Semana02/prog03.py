#Autor: Igor Augusto
#Data: 16/03/2021

#------------------ Listas
#Declaração da Listas
courses = ['History', 'Math', 'Physics', 'Comp Sci']

courses_2 = ['Health', 'Biology', 'Sociology']

nums= [1,5,2,4,3]

#Imprimindo a Lista declarada
print(courses)

#Comprimento da lista declarada
print(len(courses))

#Imprimir o terceiro valor da lista, lembrando que começa em zero
print(courses[3]) #Resultado Comp Sci

#Imprimir o último item da lista
print(courses[-1]) #Resultado Comp Sci

#Foi mostrado como acessar indices da lista, conforme vídeo 2

#Para inserir algo no final da lista, utilize o append
courses.append('Art')

#Para inserir algo no inicio da lista, utilize o insert
courses.insert(0,'Art')

print(courses)

#Para inserir algo na lista utilizando o método extend
courses.extend(courses_2)

#Para remover algo da lista
courses.remove('Art')

#Para remover o último valor da lista utilize o pop
courses.pop()

#Para imprimir a lista reverso
courses.reverse()

#Para classificar a lista em ordem alfabetica
courses.sort()

#Para classificar do menor para o maior
nums.sort()

#Para classificar do maior para o menor
nums.sort(reverse=True)

print(nums)

#Para pegar o menor valor da lista
print(min(nums))

#Para pegar o maior valor da lista
print(max(nums))

#Para pegar a soma dos valores da lista
print(sum(nums))

#Para identificar o índice de um dos valores da lista
print(courses.index('Art'))

#Para verificar se um valor esta na lista
print('Math' in courses)

print (courses)

#Inicio For para percorrer todos os items da nossa lista (courses)
#Ele vai imprimir cada item em uma linha devido a instrução PERT
for item in courses:
        print(item)

#Inicio For para percorrer todos os items da nossa lista (courses)
for course in courses:
    print(course)

#For utilizando a função enumerar, vai retornar dois valores: índice e o valor
#Se eu não quiser começar com o índice 0, basta inserir o start
for index, course in enumerate(courses, start =1):
    print(index, course)

#---Função Join
#Para imprimir a função sem as aspas simples (') e separadas por vírgula
courses_str = ', '.join(courses)
print(courses_str)


#TUPLAS
#Tuplas são diferentes de listas, tuplas não são mutáveis enquanto listas são
#Para diferenciar uma tupla de uma lista basta mudar de colchetes (mutável) para parenteses (imutável)

Lista = ['Math', 'Biology', 'Engineering']
Tupla = ('Math', 'Biology', 'Engineering')

#Conjuntos
#Observe que para os conjuntos usam-se chaves para iniciar e finalizar
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)
