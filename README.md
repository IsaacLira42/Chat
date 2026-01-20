# Chat Distribuído Simples com TCP, UDP e gRPC

## 📌 Introdução

Este projeto foi desenvolvido como um **estudo de caso acadêmico** com o objetivo de demonstrar, de forma prática e simples, o uso dos **protocolos de comunicação TCP, UDP e gRPC**, explorando as características e responsabilidades específicas de cada um.

A solução proposta consiste em um **sistema de chat distribuído**, no qual múltiplos clientes podem se conectar remotamente a um servidor central para trocar mensagens de texto. O projeto foi construído priorizando **simplicidade, clareza arquitetural e aderência estrita aos requisitos**, sem o uso de abstrações como HTTP, REST, WebSocket ou frameworks de alto nível.

---

## 🎯 Objetivo

O principal objetivo do projeto é:

* Demonstrar a **transmissão direta de dados utilizando TCP e UDP**
* Implementar a comunicação **exclusivamente via gRPC** para persistência e consulta de dados
* Utilizar **mais de um protocolo em um único projeto**
* Empregar **linguagens diferentes** no uso do gRPC
* Permitir testes reais de comunicação entre **máquinas distintas na rede**

---

## 🧩 Contexto de Construção

O sistema foi pensado para ser:

* **Fácil de executar e testar presencialmente**
* **Compreensível do ponto de vista didático**
* **Robusto o suficiente para demonstrar comunicação cliente-servidor real**

Cada protocolo foi escolhido de acordo com seu propósito natural:

* **UDP** para descoberta do servidor
* **TCP** para troca confiável de mensagens
* **gRPC** para gerenciamento do histórico do chat

A interface do usuário é feita via **terminal**, reduzindo a complexidade e evitando dependências desnecessárias.

---

## 📖 Caso de Uso

### Cenário

Um usuário deseja participar de um chat distribuído simples.

### Fluxo de funcionamento

1. O cliente inicia a aplicação no terminal
2. O cliente envia uma mensagem via **UDP** para descobrir onde o servidor do chat está rodando
3. O servidor responde com seu **endereço IP e porta TCP**
4. O cliente estabelece uma conexão **TCP** com o servidor
5. O usuário envia mensagens no formato **(usuário, mensagem)**
6. O servidor recebe e repassa as mensagens para todos os clientes conectados
7. Cada mensagem recebida é armazenada utilizando um **serviço gRPC**
8. O histórico de mensagens pode ser consultado por um cliente gRPC separado

---

## 🔌 Uso dos Protocolos

### UDP — Descoberta do Servidor

Utilizado para que o cliente descubra dinamicamente o endereço do servidor de chat na rede, sem necessidade de configuração manual.

### TCP — Comunicação do Chat

Responsável pela troca confiável de mensagens entre clientes e servidor, garantindo entrega e ordem correta.

### gRPC — Histórico de Mensagens

Utilizado para armazenar e consultar o histórico do chat, garantindo comunicação estruturada e tipada entre serviços desenvolvidos em **linguagens diferentes**.

---

## 🛠️ Tecnologias Utilizadas

* **Python**

  * Sockets TCP e UDP (`socket`)
  * Servidor gRPC
* **Node.js**

  * Cliente gRPC
* **Protocol Buffers (protobuf)**
* **Git e GitHub** para versionamento

---

## 📂 Estrutura do Projeto

```
chat/
│
├── server/
│   ├── udp_server.py       # Server UDP
│   ├── tcp_server.py       # Server TCP
│   └── grpc_server.py      # Server gRPC
│
├── client/
│   ├── udp_client.py       # Descoberta do Server
│   ├── tcp_client.py       # Comunicação (Chat)
│   └── main.py             # Arquivo Principal que Unifica os 2 Clientes
│
├── grpc-client/
│   └── client.js           # Cliente para Verificação de Histórico do Chat
│
├── grpc/
│   └── chat.proto          # Contrato de Comunicação gRPC
│
├── requirements.txt        # Arquivo Contendo as Dependências Necessárias para o Chat (Python)
│
└── README.md               # Documentação da Atividade
```

---

## ▶️ Como Executar o Projeto

### Pré-requisitos

* Python 3.10 ou superior
* Node.js 18 ou superior
* Git instalado

---

### 1️⃣ Instalação das dependências

Clone o repositório e instale as dependências necessárias.

```bash
Python
pip install -r requirements.txt
```

```bash
Node.js
cd grpc-client
npm install
```

---

### 2️⃣ Executar o servidor

Em uma máquina (ou terminal), execute os serviços do servidor:

```bash
python server/udp_server.py
python server/tcp_server.py
python server/grpc_history_server.py
```

#### ⚠️ Esses serviços podem ser executados em terminais separados ou em segundo plano.

---

### 3️⃣ Executar o cliente

Em outra máquina ou no mesmo computador, execute o cliente do chat:

```bash
python client/main.py
```

#### ⚠️ Siga as instruções no terminal para informar o nome de usuário e enviar mensagens.

---

### 4️⃣ (Opcional) Consultar o histórico via gRPC

Para consultar o histórico de mensagens armazenado, execute o cliente gRPC:

```bash
node grpc-client/client.js
```

---

## 🧪 Testes Presenciais

O projeto permite:

* Conectar múltiplos clientes simultaneamente
* Testar comunicação entre máquinas diferentes
* Verificar mensagens em tempo real
* Consultar histórico armazenado via gRPC

---

## 📌 Observações Finais

* O projeto **não utiliza HTTP, REST, WebSocket ou frameworks de abstração**
* Os protocolos **TCP e UDP são usados diretamente**
* O gRPC é utilizado exclusivamente para transmissão de dados estruturados
* A simplicidade da solução facilita a validação e a apresentação presencial

---

## 👨‍💻 Autores

### [DevJoaoVitorB](https://github.com/DevJoaoVitorB)

### [IsaacLira42](https://github.com/IsaacLira42)
