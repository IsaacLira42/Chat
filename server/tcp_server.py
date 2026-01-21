import socket
import threading
import grpc
import chat_pb2
import chat_pb2_grpc

# ATUALIZADO PARA O SEU IP ATUAL
IP_HOST = "192.168.0.9"        
TCP_IP = "0.0.0.0"              
TCP_PORT = 7000                 

# Conexão com o servidor gRPC
channel = grpc.insecure_channel(IP_HOST + ":8000")
stub = chat_pb2_grpc.ChatHistoryStub(channel)

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            decoded_message = message.decode().strip()
            if ":" in decoded_message:
                user, text = decoded_message.split(":", 1)
            else:
                user, text = "desconhecido", decoded_message

            stub.SaveMessage(chat_pb2.MessageRequest(user=user.strip(), text=text.strip()))
            
            for client in clients:
                if client != client_socket:
                    client.send(message)
        except:
            break
    
    if client_socket in clients:
        clients.remove(client_socket)
    client_socket.close()

if __name__ == "__main__":
    socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_tcp.bind((TCP_IP, TCP_PORT))
    socket_tcp.listen()
    print(f"🚀 Servidor TCP ativo em {IP_HOST}:{TCP_PORT}")

    while True:
        client_socket, client_address = socket_tcp.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()