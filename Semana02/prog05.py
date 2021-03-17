#Autor: Igor Augusto
#Data: 16/03/2021


# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

language = 'Phyton'

if language == 'Phyton':
   print('É Phyton')

else:
    print('É falso')

#Verificando se a linguagem é phyton, se não for verifica se é Java e se não for faça
if language == 'Phyton':
   print('É Phyton')
elif language =='Java':
    print('É Java')
else:
    print('É falso')

    a = [1,2,3]
    b = [1,2,3]

    print(a == b)



