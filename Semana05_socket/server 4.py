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

#definir o objeto socket. Socket é um ponto final, não é em si a comunicação
server_socket = socket . socket ( socket . AF_INET , socket . SOCK_STREAM )
server_socket . setsockopt ( socket . SOL_SOCKET , socket . SO_REUSEADDR , 1 ) 

#iniciando a conexão com o servidor
server_socket.bind((IP, PORT))
server_socket.listen()

# tupla de soquetes para selecionar e acompanhar, bem como começar nosso clientsdict:
sockets_list = [server_socket]
clients = {}

#saída informando da conexão
print(f'Listening for connections on {IP}:{PORT}...')

#A principal função deste servidor é receber mensagens e depois distribuir para os clientes conectados via broadcast. 
#Função para receber mensagens
def receive_message(client_socket):
    try:
        # ler o cabeçalho:
        message_header = client_socket.recv(HEADER_LENGTH)

        #caso o cliente feche a conexão normalmente será enviado um socket.close() e não haverá nenhum cabeçalho
        if not len(message_header):
            return False
              # tamanho do cabeçalho:
            message_length = int(message_header.decode('utf-8').strip())
            return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        return False

while True:
    #loop para receber mensagem de todos os sockets de nossos clientes e envia as mensagens para todos os sockets de clientes
     read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

     #Vamos iterar a read_socketslista
    for notified_socket in read_sockets:
        #Se o soquete notificado for o soquete do nosso servidor significa que acabamos de obter uma nova conexão
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            #Se o soquete notificado for falso, continua até ser verdadeiro
            if user is False:
                continue
            #acrescentar novo client_socket ao sockets_list
                sockets_list.append(client_socket)
                clients[client_socket] = user
                print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
            #Se o soquete notificado não for um soquete de servidor significa que tem uma mensagem para ler:
        else:
            message = receive_message(notified_socket)
            #Antes de tentarmos ler a mensagem, vamos ter certeza de que existe uma. Se o cliente se desconectar, a mensagem ficará vazia:
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                sockets_list.remove(notified_socket)
                del clients[notified_socket]

                continue
            #Supondo que não foi uma desconexão, podemos ler as informações assim:     
            user = clients[notified_socket]
            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            #Iterar sobre clientes conectados e transmitir mensagem
            for client_socket in clients:
                # Mas não o envie ao remetente
                if client_socket != notified_socket:
                # Enviar usuário e mensagem ambos com seus cabeçalhos 
                client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
    for notified_socket in exception_sockets:
    # Remove da lista socket.socket()
        sockets_list.remove(notified_socket)
        # Remove de outras listas de usuários
        del clients[notified_socket]