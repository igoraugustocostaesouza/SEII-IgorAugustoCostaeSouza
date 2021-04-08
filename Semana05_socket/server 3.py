#Igor Augusto - 11221EMT008

import socket

#importando a biblioteca time
import time

#importando pickle
import pickle

#constante que irá conter o tamanho do cabeçalho
HEADERSIZE = 10

#definir o objeto socket. Socket é um ponto final, não é em si a comunicação
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#hospedando o servidor cuja porta é 1234
s.bind((socket.gethostnome(),1235))

#servidor com uma fila de no máximo cinco
s.listen(5)

while True:
    #o socket do cliente e o endereço é como se fosse o IP
    clientsocket, address = s.accept()

    #imprimindo algumas informações
    printf(f"Connection from{adress} has been established!")

    #criando um dicionário para exemplificar a serialização
    d = {1: "Hey", 2:"There"} 
    msg = pickle.dumps(d)
   
    #convertendo em bytes a mensagem com tamanho de 8
    msg = bytes(f'{len(msg):<{HEADERSIZE}}',"utf-8")+msg

    #declarando o cliente que vai mandar a mensagem, os bytes e os tipos
    clientesocket.send(msg) 


 
