#Autor: Igor Augusto
#Data: 16/03/2021

#Definição da string contendo as keys
student = {'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

#para adicionar uma nova relação na string student
student['phone']='555-5555'

#Saída é a string
print(student)

#Saída é a relação com os courses
print(student['courses'])

#Saída é a relação com o campo name
print(student['name'])

#Outra forma de acesso é através do get
print(student.get('courses', 'Not Found'))
print(student.get('phone', 'Not Found'))

#Para atualizar a string, basta
student.update ({'name':'Jane', 'age':'30', 'phone':'555-55555'})

#Para excluir a idade dos alunos
#del student['age']

print(student)

#Removendo através do método POP
age = student.pop('age')

#imprimindo o valor removido
print(age)

#Para ver a quantidade de chaves
print(student.keys())

#Para ver quais as chaves
print(len(student))

#for para percorrer todas as chaves
for key in student:
    print(key)

#for para percorrer as chaves e os valores
for key, value in student.items():
    print(key, value)

