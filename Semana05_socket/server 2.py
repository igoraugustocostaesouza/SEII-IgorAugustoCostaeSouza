#Igor Augusto - 11221EMT008


#importando o socket através de uma biblioteca
import socket

#importando a biblioteca time
import time

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

    #mensagem de boas vindas quando o cliente entra no servidor
    msg="Welcome to the server!"

    #imprimir a string F que verifica se tem menos de 10 caracteres e adiciona a msg de boas vindas
    msg = f'{len(msg):<{HEADERSIZE}}'+msg

    #declarando o cliente que vai mandar a mensagem, os bytes e os tipos
    clientesocket.send(bytes(msg, "utf-8")) 

#inserindo um loop para poder ficar enviando msg pro servidor mostrando que a conexão ainda está ativa
while True:
    #aqui vai colocar um delay de 3 segundos para o programa
    time.sleep(3)
    #print na tela mostrando a hora que recebemos a mensagem de tamanho do cabeçalho
    msg = f"The time is! {time.time()}"
    msg = f'{len(msg):<{HEADERSIZE}}'+msg
    clientesocket.send(bytes(msg, "utf-8")) 
 
