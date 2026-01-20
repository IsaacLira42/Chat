import socket
from tcp_server import IP_HOST, TCP_PORT 

# VARIAVEIS DE AMBIENTE
UDP_IP = "0.0.0.0"  # IP do Servidor UDP - "escutar em todas as interfaces de rede"
UDP_PORT = 8080     # Porta do Servidor UDP

socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # Rede IPv4 + Datagrama UDP

socket_udp.bind((UDP_IP, UDP_PORT))                             # Definir para onde as mensagens serão enviadas - tupla de IP:Porta 

print("🚀Servidor UDP ativo \n")

while True:
    '''
        1 - Esperando mensagens
        - Pacotes <= 1024 bytes
        - Recebe -> mensagem (data) + IP + Portas do remetente (address)

        2 - Interpretar mensagem 
        - Decodificar os bytes

        3 - Enviar resposta 
        - Formato -> IP:PORT 
        - Localização do servidor do Chat TCP para o endereço do remetente
    '''

    data, address = socket_udp.recvfrom(1024)

    message = data.decode()

    # DEBUG
    print(f"Mensagem Recebida: {message} - Endereço: {address}")

    # Não recebe mensagens desconhecidas, apenas de descoberta do servidor do chat "DISCOVER_CHAT"
    if message == "DISCOVER_CHAT":
        response = f"{IP_HOST}:{TCP_PORT}"
        socket_udp.sendto(response.encode(), address)
