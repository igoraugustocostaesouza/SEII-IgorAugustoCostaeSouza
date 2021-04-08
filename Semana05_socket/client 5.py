#Igor Augusto - 11221EMT008

#importando o socket através de uma biblioteca
import socket
 import select
#constante que irá conter o tamanho do cabeçalho
HEADERSIZE = 10
#hospedando o servidor cujo endereço de IP é
IP = "127.0.0.1" 
#hospedando o servidor cuja porta é 1234
PORT = 1234
#definindo o nome de usuário
my_username = input("Username: ")
#definir o objeto socket. Socket é um ponto final, não é em si a comunicação
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Conectando a porta e ip informado
client_socket.connect((IP, PORT))
# Define a conexão para o estado sem bloqueio para que a chamada .recv não tenha bloqueio
client_socket.setblocking(False)
#Informa o nome de usuário e o cabeçalho para enviar
#Codificando o nome de usuário em bytes 
username = my_username.encode('utf-8')
#contar o número de bytes e #preparar o cabeçalho de tamanho fixo, que codificaremos também em bytes 
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    #Aguardando que o usuário insira uma mensagem
    message = input(f'{my_username} > ')
    #Se a mensagem não for vazia
    if message:
        #Codificar a mensagem em bytes
        message = message.encode('utf-8')
        #prepara o cabeçalho 
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        #envia a mensagem
        client_socket.send(message_header + message)

    try:
        #loop sobre as mensagens recebidas
        while True:
             # Receba o cabeçalho da mensagem com o comprimento do nome de usuário 
            username_header = client_socket.recv(HEADER_LENGTH)

           #se não houver dados a conexão é fechada
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            #Convertendo o cabeçalho para inteiro
            username_length = int(username_header.decode('utf-8').strip())

            #Recebe e decodifica o usuário
            username = client_socket.recv(username_length).decode('utf-8')

            #recebe a mensagem inteira
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            print(f'{username} > {message}')

    except IOError as e:
        #conexão para tratativa de erro que podem ser geradas no SO, mais detalhes ver o vídeo 
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        #se não receber nenhum erro para tratar, continua
        continue

    except Exception as e:
        # se veio outro erro não mapeado, imprima o erro
        print('Reading error: '.format(str(e)))
        sys.exit()