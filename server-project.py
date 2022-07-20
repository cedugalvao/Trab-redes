import socket
import threading

host = 'localhost'
port = 59993
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adress = (host, port)

# metodo bind vincular porta com endereço ip
server.bind(adress)

# metodo listen server esta esperando uma conexão
server.listen()

# lista de clientes e nicknames(apelidos)
clients = []
apelidos = []

# funcao para estabelecimento de conexao com o cliente


def conexao(client):
    while True:
        try:
            message = client.recv(1024)
            for client in clients:
                client.send(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            apelido = apelidos[index]
            tam = len(clients)
            for i in range(tam):
                print(f'o usuario {apelido} foi desconectado'.encode('utf-8'))

            apelidos.remove(apelido)
            break


def main():
    while True:
        print('Server esta funcionando')
        client, address = server.accept()
        nome_do_pc = socket.gethostname()
        ip_do_pc = socket.gethostbyname(nome_do_pc)
        print(f'conexao estabelecida com {ip_do_pc} e porta {str(port)}')
        client.send('pressione enter para confirmar'.encode('utf-8'))
        apelido = client.recv(1024).decode("utf-8")
        apelidos.append(apelido)
        clients.append(client)
        print(f'O usuario {apelido} entrou na sala'.encode('utf-8'))

        for client in clients:
            print(f'{apelido} esta conectado na sala'.encode('utf-8'))

        client.send('você esta conectado!\n'.encode('utf-8'))

        thread = threading.Thread(target=conexao, args=(client,))
        print(f'usuarios ativos: {threading.active_count()}')
        thread.start()


main()
