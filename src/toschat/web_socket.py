import threading
import socket


WEB_SOCKET_HOST = "127.0.0.1"
WEB_SOCKET_PORT = 59000
MAX_BYTE = 1024


def connect_websocket_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((WEB_SOCKET_HOST, WEB_SOCKET_PORT))
    return client


def websocket_receive_message(client):
    while True:
        try:
            message = client.recv(MAX_BYTE).decode("utf-8")
        except:
            client.close()
            break


def websocket_send_message(client, message):
    client.send(message.encode("utf-8"))


