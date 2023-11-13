import threading
import socket


WEB_SOCKET_HOST = "127.0.0.1"
PORT = 59000
MAX_BYTE = 2014

server = None
clients = []


def init_websocket_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((WEB_SOCKET_HOST, PORT))
    server.listen()


# send message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)


def handle_receiving_message(client):
    while True:
        try:
            message = client.recv(MAX_BYTE)
            broadcast(message)  
        except:
            # something went wrong
            # disconnect client from socket connection
            # index = clients.index(client)
            clients.remove(client)
            client.close()
            break


def listen_to_client_connection():
    while True:
        client, address = server.accept()
        clients.append(client)

        print("client has connected to socket server")

        thread = threading.Thread(target=handle_receiving_message, args=(client,))
        thread.start()


if __name__ == "__main__":
    listen_to_client_connection()
