import socket

def discover_server():
    UDP_PORT = 8080
    # ATUALIZADO PARA O IP DO SERVIDOR
    DEST_IP = "192.168.0.9" 
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3.0) 

    try:
        print(f"🔍 Buscando servidor em {DEST_IP}:{UDP_PORT}...")
        sock.sendto("DISCOVER_CHAT".encode(), (DEST_IP, UDP_PORT))
        
        data, address = sock.recvfrom(1024)
        print(f"✅ Servidor encontrado: {data.decode()}")
        return data.decode().split(":") 
    except socket.timeout:
        print("❌ Erro: O servidor não respondeu no IP 192.168.0.9.")
        return None
    finally:
        sock.close()