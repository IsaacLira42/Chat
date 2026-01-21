import socket
from tcp_server import IP_HOST, TCP_PORT 

UDP_IP = "0.0.0.0" 
UDP_PORT = 8080

if __name__ == "__main__":
    socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        socket_udp.bind((UDP_IP, UDP_PORT))
        print(f"🚀 Servidor UDP ativo na porta {UDP_PORT}")
        print(f"📢 Respondendo como: {IP_HOST}:{TCP_PORT}")
    except Exception as e:
        print(f"❌ Erro ao iniciar UDP: {e}")

    while True:
        data, address = socket_udp.recvfrom(1024)
        message = data.decode().strip()

        print(f"📩 Requisição de descoberta vinda de: {address}")

        if message == "DISCOVER_CHAT":
            response = f"{IP_HOST}:{TCP_PORT}"
            socket_udp.sendto(response.encode(), address)
            print(f"✅ Resposta enviada para {address}")