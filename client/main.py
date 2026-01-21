from udp_client import discover_server
from tcp_client import start_chat

def main():
    print("=== CLIENTE DE CHAT DISTRIBUÍDO ===")
    username = input("Digite seu nome de usuário: ").strip()
    
    if not username:
        username = "Anônimo"

    # 1. Descoberta via UDP [cite: 40]
    server_info = discover_server()
    
    if server_info:
        ip, port = server_info
        # 2. Iniciar Chat via TCP [cite: 30]
        start_chat(ip, port, username)
    else:
        print("Não foi possível iniciar o chat sem o endereço do servidor.")

if __name__ == "__main__":
    main()