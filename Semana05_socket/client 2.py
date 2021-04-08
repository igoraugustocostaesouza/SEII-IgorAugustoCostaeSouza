#Igor Augusto - 11221EMT008

#importando o socket através de uma biblioteca
import socket


#constante que irá conter o tamanho do cabeçalho
HEADERSIZE = 10

#definir o objeto socket. Socket é um ponto final, não é em si a comunicação
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#informar novamente o IP e a porta que desejamos conectar. No geral...
#vamos utilizar o servidor local, porém na prática teremos que conectar...
#a um IP remoto
s.connect((socket.gethostname(),1235))

#loop para a verdadeira mensagem completar, caso mensagem seja menor que 10
while True:

    #declarando a msg como vazia
    full_msg = ''

    #mensagem atualizada contendo o tamanho correto
    new_msg = ''

    #comando while para executar novamente o código e receber a mensagem de boas vindas
    while True:

        # soquete TCP com pacote de dados de 1024 bytes, o tamanho fica a cargo do programador dependendo do tamanho do arquivo que se quer mandar
        msg = s.recv(16)

        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            #capturar o verdadeiro tamanho da mensagem
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg+=msg.decode("utf=")
        #verificando o tamanho da nova mensagem
            if len (full_msg) - HEADERSIZE == msglen:
                    #aparece no display que a mensagem foi recebida
                    print("full msg recvd")
                    print(full_msg[HEADERSIZE:])
                    #coloca a nova mensagem como verdade
                    new_msg = True
                    full_msg = ''
        #imprimir a decodificaçao da mensagem
        print(full_msg)