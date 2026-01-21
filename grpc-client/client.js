const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const path = require('path');

// Carrega o arquivo .proto
const PROTO_PATH = path.resolve(__dirname, '../grpc/chat.proto');
const packageDefinition = protoLoader.loadSync(PROTO_PATH);
const chatProto = grpc.loadPackageDefinition(packageDefinition).chat;

function main() {
    // Endereço do servidor gRPC (mesmo IP_HOST configurado no Python)
    const target = '192.168.0.9:8000'; 
    const client = new chatProto.ChatHistory(target, grpc.credentials.createInsecure());

    console.log("--- Consultando Histórico de Mensagens ---");

    client.ListMessages({}, (err, response) => {
        if (err) {
            console.error("Erro ao buscar histórico:", err.details);
            return;
        }

        if (response.messages && response.messages.length > 0) {
            response.messages.forEach(msg => {
                console.log(`[${msg.user}]: ${msg.text}`);
            });
        } else {
            console.log("O histórico está vazio.");
        }
    });
}

main();