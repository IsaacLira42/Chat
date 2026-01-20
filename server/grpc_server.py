from concurrent import futures
import grpc

import chat_pb2
import chat_pb2_grpc

# Armazena o histórico de mensagens em memória
messages = []


class ChatHistoryService(chat_pb2_grpc.ChatHistoryServicer):
    """
    Implementação do serviço definido no arquivo chat.proto.

    Responsável por:
    - Salvar mensagens recebidas
    - Retornar o histórico completo de mensagens
    """

    def SaveMessage(self, request, context):
        """
        RPC responsável por salvar uma nova mensagem no histórico.

        Parâmetros:
        - request.user: nome do usuário que enviou a mensagem
        - request.text: conteúdo da mensagem

        Retorno:
        - Empty (confirma apenas que a operação foi concluída)
        """

        messages.append({
            "user": request.user,
            "text": request.text
        })

        return chat_pb2.Empty()

    def ListMessages(self, request, context):
        """
        RPC responsável por retornar todas as mensagens salvas.

        Retorna:
        - MessageList contendo uma lista de mensagens
        """

        response = chat_pb2.MessageList()

        for msg in messages:
            response.messages.add(
                user=msg["user"],
                text=msg["text"]
            )

        return response


def serve():
    """
    Inicializa e executa o servidor gRPC.

    - Cria um pool de threads para atender múltiplas requisições
    - Registra o serviço ChatHistoryService
    - Escuta na porta 8000
    """

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    chat_pb2_grpc.add_ChatHistoryServicer_to_server(
        ChatHistoryService(),
        server
    )

    # Porta onde o serviço gRPC ficará disponível
    server.add_insecure_port("[::]:8000")

    server.start()
    print("🚀 Servidor gRPC ativo\n")

    # Mantém o servidor em execução
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
