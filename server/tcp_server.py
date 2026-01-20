import socket
import threading

# VARIAVEIS DE AMBIENTE
IP_HOST = "192.168.0.10"        # IP da Máquina do Servidor TCP (substituir pelo IP da maquina do server TCP - Ex.: 192.168.X.X)
TCP_IP = "0.0.0.0"              # IP do Servidor TCP - "escutar em todas as interfaces de rede"
TCP_PORT = 7000                 # Porta do Servidor TCP

socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Rede IPv4 + Datagrama TCP

socket_tcp.bind((TCP_IP, TCP_PORT))                                 # Definir para onde as mensagens serão enviadas - tupla de IP:Porta

socket_tcp.listen()                                                 # Esta aberto para receber mensagens

clients = []                                                        # Lista de clientes conectados

print("🚀Servidor TCP ativo \n")

def handle_client(client_socket):
    '''
        Função de Gerenciamento de Thread
        - Recebe mensagens
        - Repassa para os outros clientes

        OBS.: "recv" retorna vazio quando o cliente desconecta.
    '''
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break

            # DEBUG
            print(f"Mensagem - {message}")
            
            # Enviar mensagens para todos os clientes conectados
            for client in clients:
                if client != client_socket:
                    client.send(message)

        except:
            break
    
    # DEBUG
    print(f"Cliente desconectado!")

    clients.remove(client_socket)
    client_socket.close()

while True:
    '''
        1 - Conexão estabelecida
        - Recebe -> Canal direto do cliente (client_socket) + IP + Portas do cliente (client_address)

        2 - Adicionar cliente a lista de clientes conectados

        3 - Thread (> 1 Cliente Simultâneo) 
    '''

    client_socket, client_address = socket_tcp.accept()

    # DEBUG
    print(f"Cliente conectado: {client_address}")

    clients.append(client_socket)

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket,)
    )
    thread.start()
