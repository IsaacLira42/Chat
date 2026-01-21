import socket
import threading
import sys

def receive_messages(sock):
    """Thread para escutar mensagens vindas do servidor."""
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print(f"\n{msg}")
            print("> ", end="", flush=True) # Mantém o prompt de digitação
        except:
            break

def start_chat(ip, port, username):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_sock.connect((ip, int(port)))
        
        # Inicia thread para receber mensagens sem bloquear a digitação
        threading.Thread(target=receive_messages, args=(client_sock,), daemon=True).start()

        print(f"--- Bem-vindo ao Chat, {username}! (Digite 'sair' para encerrar) ---")
        while True:
            text = input("> ")
            if text.lower() == 'sair':
                break
            
            # Formato esperado pelo seu tcp_server.py: "usuario: mensagem" [cite: 33]
            full_message = f"{username}: {text}"
            client_sock.send(full_message.encode())
            
    except Exception as e:
        print(f"Erro de conexão: {e}")
    finally:
        client_sock.close()