#Igor Augusto - 11221EMT008

#importando o socket através de uma biblioteca
import socket

#definir o objeto socket. Socket é um ponto final, não é em si a comunicação
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#informar novamente o IP e a porta que desejamos conectar. No geral...
#vamos utilizar o servidor local, porém na prática teremos que conectar...
#a um IP remoto
s.connect((socket.gethostname(),1234))

#declarando a msg como vazia
full_msg = ''

#comando while para executar novamente o código e receber a mensagem de boas vindas
while True:

    # soquete TCP com pacote de dados de 1024 bytes, o tamanho fica a cargo do programador dependendo do tamanho do arquivo que se quer mandar
    msg = s.recv(8)

    #verificando se a mensagem é menor ou igual a zero
    if len(msg)<=0:
    break

    full_msg+=msg.decode("utf=")

    #imprimir a decodificaçao da mensagem
    print(full_msg)