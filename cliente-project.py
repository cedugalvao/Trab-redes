import socket
import threading

apelido = input('como vc gostaria de ser chamado?\n')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor = ('localhost', 59993)
client.connect(servidor)


def c_recv():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == "apelido":
                client.send(apelido.encode('utf-8'))
            else:
                print(msg)
        except:
            print('-1\nvoce foi desconectado do server')
            client.close()
            break


def c_send():
    while True:
        msg = f'{apelido}: {input("")}'
        client.send(msg.encode('utf-8'))


threading.Thread(target=c_recv).start()
send_thread = threading.Thread(target=c_send).start()
