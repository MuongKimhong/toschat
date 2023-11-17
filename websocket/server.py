import threading
import socket


WEB_SOCKET_HOST = "127.0.0.1"
PORT = 59000
MAX_BYTE = 2014

server = None
clients = []


# init websocket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((WEB_SOCKET_HOST, PORT))
server.listen()


# send message to all clients
def broadcast(message):
    print("forward message")
    for client in clients:
        client.send(message)


def handle_receiving_message(client):
    while True:
        try:
            message = client.recv(MAX_BYTE)
            print("message receive") 
            broadcast(message)  
        except:
            # something went wrong
            # disconnect client from socket connection
            # index = clients.index(client)
            print("something wrong")
            clients.remove(client)
            client.close()
            break


# listen to event when users connect to websocket server
def listen_to_client_connection():
    while True:
        client, address = server.accept()
        clients.append(client)

        print("client has connected to socket server")

        thread = threading.Thread(target=handle_receiving_message, args=(client,))
        thread.start()


if __name__ == "__main__":
    listen_to_client_connection()
