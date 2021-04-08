#Igor Augusto - 11221EMT008

#importando o socket através de uma biblioteca
import socket

#definir o objeto socket. Socket é um ponto final, não é em si a comunicação
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#hospedando o servidor cuja porta é 1234
s.bind((socket.gethostnome(),1234))

#servidor com uma fila de no máximo cinco
s.listen(5)

while True:
    #o socket do cliente e o endereço é como se fosse o IP
    clientsocket, address = s.accept()

    #imprimindo algumas informações
    printf(f"Connection from{adress} has been established!")

    #declarando o cliente que vai mandar a mensagem, os bytes e os tipos
    clientesocket.send(bytes("Welcome to the server!", "utf-8"))

    #fechando a conexão com o cliente
    clientsocket.close()
